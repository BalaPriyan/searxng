# SPDX-License-Identifier: AGPL-3.0-or-later
# pyright: basic
"""
 Wikipedia (Web)
"""

from urllib.parse import quote
from json import loads
from typing import List
from lxml.html import fromstring
from searx.engine import (
    About,
    InfoBox,
    OnlineEngine,
    QueryContext,
    OnlineRequest,
    Result,
    Response,
    StandardResult,
)
from searx.utils import match_language, searx_useragent, find_language_aliases
from searx.network import raise_for_httperror
import searx.data

# about
about: About = {
    "website": 'https://www.wikipedia.org/',
    "wikidata_id": 'Q52',
    "official_api_documentation": 'https://en.wikipedia.org/api/',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

# search-url
search_url = 'https://{language}.wikipedia.org/api/rest_v1/page/summary/{title}'
supported_languages_url = 'https://meta.wikimedia.org/wiki/List_of_Wikipedias'
language_variants = {"zh": ("zh-cn", "zh-hk", "zh-mo", "zh-my", "zh-sg", "zh-tw")}


class WikipediaEngine(OnlineEngine):
    about = about
    supported_languages = searx.data.ENGINES_LANGUAGES['wikipedia']
    language_aliases = find_language_aliases(supported_languages)

    def _url_lang(self, lang: str):
        lang_pre = lang.split('-')[0]
        if lang_pre == 'all' or lang_pre not in self.supported_languages and lang_pre not in self.language_aliases:
            return 'en'
        return match_language(lang, self.supported_languages, self.language_aliases).split('-')[0]

    def request(self, query: str, ctx: QueryContext) -> OnlineRequest:
        if query.islower():
            query = query.title()

        language = self._url_lang(ctx.language)

        req = OnlineRequest(
            url=search_url.format(title=quote(query), language=language),
            raise_for_httperror=False,
            soft_max_redirects=2,
            headers={'User-Agent': searx_useragent()},
        )

        if ctx.language.lower() in language_variants.get(language, []):
            req.set_header('Accept-Language', ctx.language.lower())

        return req

    def response(self, resp: Response) -> List[Result]:
        if resp.status_code == 404:
            return []

        if resp.status_code == 400:
            try:
                api_result = loads(resp.text)
            except:
                pass
            else:
                if (
                    api_result['type'] == 'https://mediawiki.org/wiki/HyperSwitch/errors/bad_request'
                    and api_result['detail'] == 'title-invalid-characters'
                ):
                    return []

        raise_for_httperror(resp)

        results: List[Result] = []
        api_result = loads(resp.text)

        # skip disambiguation pages
        if api_result.get('type') != 'standard':
            return []

        title = api_result['title']
        wikipedia_link = api_result['content_urls']['desktop']['page']

        results.append(StandardResult(url=wikipedia_link, title=title))

        results.append(
            InfoBox(
                url=wikipedia_link,
                title=title,
                content=api_result.get('extract', ''),
                img_src=api_result.get('thumbnail', {}).get('source'),
                links=[{'title': 'Wikipedia', 'url': wikipedia_link}],
            )
        )

        return results


# get supported languages from their site
def _fetch_supported_languages(resp):
    supported_languages = {}
    dom = fromstring(resp.text)
    tables = dom.xpath('//table[contains(@class,"sortable")]')
    for table in tables:
        # exclude header row
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            td = tr.xpath('./td')
            code = td[3].xpath('./a')[0].text
            name = td[2].xpath('./a')[0].text
            english_name = td[1].xpath('./a')[0].text
            articles = int(td[4].xpath('./a/b')[0].text.replace(',', ''))
            # exclude languages with too few articles
            if articles >= 100:
                supported_languages[code] = {"name": name, "english_name": english_name}

    return supported_languages
