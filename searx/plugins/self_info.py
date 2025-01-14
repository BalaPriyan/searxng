# SPDX-License-Identifier: AGPL-3.0-or-later
# pylint: disable=missing-module-docstring, missing-class-docstring
from __future__ import annotations
import typing

import re
from flask_babel import gettext

from searx.botdetection._helpers import get_real_ip
from searx.result_types import Answer

from . import Plugin, PluginInfo

if typing.TYPE_CHECKING:
    from searx.search import SearchWithPlugins
    from searx.extended_types import SXNG_Request


class SXNGPlugin(Plugin):
    """Simple plugin that displays information about user's request, including
    the IP or HTTP User-Agent.  The information is displayed in area for the
    "answers".
    """

    id = "self_info"
    default_on = True
    keywords = ["ip", "user-agent"]

    def __init__(self):
        super().__init__()

        self.ip_regex = re.compile(r"^ip", re.IGNORECASE)
        self.ua_regex = re.compile(r"^user-agent", re.IGNORECASE)

        self.info = PluginInfo(
            id=self.id,
            name=gettext("Self Information"),
            description=gettext(
                """Displays your IP if the query is "ip" and your user agent if the query is "user-agent"."""
            ),
            preference_section="query",
        )

    def post_search(self, request: "SXNG_Request", search: "SearchWithPlugins") -> list[Answer]:
        """Returns a result list only for the first page."""
        results = []

        if search.search_query.pageno > 1:
            return results

        if self.ip_regex.search(search.search_query.query):
            Answer(results=results, answer=gettext("Your IP is: ") + get_real_ip(request))

        if self.ua_regex.match(search.search_query.query):
            Answer(results=results, answer=gettext("Your user-agent is: ") + str(request.user_agent))

        return results
