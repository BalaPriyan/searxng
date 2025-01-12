# SPDX-License-Identifier: AGPL-3.0-or-later
"""Public domain image archive, based on the unsplash engine

"""

from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl
from json import loads

THUMBNAIL_SUFFIX = "?fit=max&h=360&w=360"
"""
Example thumbnail urls (from requests & html):
- https://the-public-domain-review.imgix.net/shop/nov-2023-prints-00043.jpg?fit=max&h=360&w=360
- https://the-public-domain-review.imgix.net/collections/the-history-of-four-footed-beasts-and-serpents-1658/8616383182_5740fa7851_o.jpg?fit=max&h=360&w=360

Example full image urls (from html)
- https://the-public-domain-review.imgix.net/shop/nov-2023-prints-00043.jpg?fit=clip&w=970&h=800&auto=format,compress
- https://the-public-domain-review.imgix.net/collections/the-history-of-four-footed-beasts-and-serpents-1658/8616383182_5740fa7851_o.jpg?fit=clip&w=310&h=800&auto=format,compress

The thumbnail url from the request will be cleaned for the full image link
The cleaned thumbnail url will have THUMBNAIL_SUFFIX added to them, based on the original thumbnail parameters
"""

# about
about = {
    "website": 'https://pdimagearchive.org',
    "use_official_api": False,
    "require_api_key": False,
    "results": 'JSON',
}

base_url = 'https://oqi2j6v4iz-dsn.algolia.net/'
search_url = (
    base_url
    + '1/indexes/*/queries?x-algolia-api-key=153d2a10ce67a0be5484de130a132050&x-algolia-application-id=OQI2J6V4IZ'
)
categories = ['images']
page_size = 20
paging = True


def clean_url(url):
    parsed = urlparse(url)
    query = [(k, v) for (k, v) in parse_qsl(parsed.query) if k not in ['ixid', 's']]

    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, urlencode(query), parsed.fragment))


def request(query, params):
    params['url'] = search_url
    params["method"] = "POST"
    params["data"] = (
        """{"requests":[{"indexName":"prod_all-images","params":"highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&"""
    )
    params["data"] += f'page={params["pageno"] - 1}&query={query}' + '"}]}'
    logger.debug("query_url --> %s", params['url'])
    return params


def response(resp):
    results = []
    json_data = loads(resp.text)

    if 'results' in json_data:
        for result in json_data['results'][0]['hits']:
            content = ""
            if "themes" in result:
                content += "Themes: " + result['themes']
            if "encompassingWork" in result:
                if content != "":
                    content += "\n"
                content += "Encompassing work: " + result['encompassingWork']

            base_image_url = result['thumbnail'].split("?")[0] if "?" in result['thumbnail'] else result['thumbnail']
            
            results.append(
                {
                    'template': 'images.html',
                    'url': clean_url(f"{about['website']}/images/{result['objectID']}"),
                    'img_src': clean_url(base_image_url),
                    'thumbnail_src': clean_url(base_image_url + THUMBNAIL_SUFFIX),
                    'title': f"{result['title'].strip()} by {result['artist']} {result.get('displayYear') or ''}",
                    'content': f"Themes: {result['themes']}",
                }
            )

    return results
