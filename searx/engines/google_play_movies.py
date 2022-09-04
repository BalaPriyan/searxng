# SPDX-License-Identifier: AGPL-3.0-or-later
# lint: pylint
"""
  Google Play Movies
"""

from json import dumps, loads
from urllib.parse import urljoin
from searx.utils import html_to_text

about = {
    "website": "https://play.google.com/",
    "wikidata_id": "Q19599426",
    "use_official_api": True,
    "require_api_key": False,
    "results": "JSON",
}

categories = ['videos']
send_accept_language_header = True

search_url = "https://play.google.com/_/PlayStoreUi/data/batchexecute"


def request(query, params):
    params["url"] = search_url

    params['method'] = 'POST'

    # can probably be shortened, but not sure how
    # fmt: off
    # pylint: disable=line-too-long
    data = [[[],[[8,[20,50]],True,None,[96,108,72,100,27,8,57,169,30,110,11,16,1,139,152,165,163,211,9,71,31,195,12,64,151,150,148,113,104,55,56,145,32,34,10,122],[None,None,[[[True],None,[[None,[]]],None,None,None,None,[None,2],None,None,None,None,None,None,None,None,None,None,None,None,None,None,[1]],[None,[[None,[]]]],[None,[[None,[]]],None,[True]],[None,[[None,[]]]],None,None,None,None,[[[None,[]]]],[[[None,[]]]]],[[[[7,1],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,31],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,104],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,9],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,8],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,27],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,12],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,65],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,110],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,88],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,11],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,56],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,55],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,96],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,10],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,122],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,72],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,71],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,64],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,113],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,139],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,150],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,169],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,165],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,151],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,163],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,32],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,16],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,108],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,100],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[7,211],[[1,73,96,103,97,58,50,92,52,112,69,19,31,101,123,74,49,80,20,10,14,79,43,42,139]]],[[9,1],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,31],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,104],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,9],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,8],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,27],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,12],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,65],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,110],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,88],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,11],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,56],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,55],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,96],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,10],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,122],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,72],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,71],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,64],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,113],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,139],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,150],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,169],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,165],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,151],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,163],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,32],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,16],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,108],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,100],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[9,211],[[1,7,9,24,12,31,5,15,27,8,13,10]]],[[17,1],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,31],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,104],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,9],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,8],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,27],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,12],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,65],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,110],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,88],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,11],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,56],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,55],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,96],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,10],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,122],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,72],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,71],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,64],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,113],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,139],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,150],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,169],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,165],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,151],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,163],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,32],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,16],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,108],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,100],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[17,211],[[1,7,9,25,13,31,5,41,27,8,14,10]]],[[10,1],[[1,7,6,9]]],[[10,31],[[1,7,6,9]]],[[10,104],[[1,7,6,9]]],[[10,9],[[1,7,6,9]]],[[10,8],[[1,7,6,9]]],[[10,27],[[1,7,6,9]]],[[10,12],[[1,7,6,9]]],[[10,65],[[1,7,6,9]]],[[10,110],[[1,7,6,9]]],[[10,88],[[1,7,6,9]]],[[10,11],[[1,7,6,9]]],[[10,56],[[1,7,6,9]]],[[10,55],[[1,7,6,9]]],[[10,96],[[1,7,6,9]]],[[10,10],[[1,7,6,9]]],[[10,122],[[1,7,6,9]]],[[10,72],[[1,7,6,9]]],[[10,71],[[1,7,6,9]]],[[10,64],[[1,7,6,9]]],[[10,113],[[1,7,6,9]]],[[10,139],[[1,7,6,9]]],[[10,150],[[1,7,6,9]]],[[10,169],[[1,7,6,9]]],[[10,165],[[1,7,6,9]]],[[10,151],[[1,7,6,9]]],[[10,163],[[1,7,6,9]]],[[10,32],[[1,7,6,9]]],[[10,16],[[1,7,6,9]]],[[10,108],[[1,7,6,9]]],[[10,100],[[1,7,6,9]]],[[10,211],[[1,7,6,9]]],[[58,1],[[5,3,1,2,6,8]]],[[58,31],[[5,3,1,2,6,8]]],[[58,104],[[5,3,1,2,6,8]]],[[58,9],[[5,3,1,2,6,8]]],[[58,8],[[5,3,1,2,6,8]]],[[58,27],[[5,3,1,2,6,8]]],[[58,12],[[5,3,1,2,6,8]]],[[58,65],[[5,3,1,2,6,8]]],[[58,110],[[5,3,1,2,6,8]]],[[58,88],[[5,3,1,2,6,8]]],[[58,11],[[5,3,1,2,6,8]]],[[58,56],[[5,3,1,2,6,8]]],[[58,55],[[5,3,1,2,6,8]]],[[58,96],[[5,3,1,2,6,8]]],[[58,10],[[5,3,1,2,6,8]]],[[58,122],[[5,3,1,2,6,8]]],[[58,72],[[5,3,1,2,6,8]]],[[58,71],[[5,3,1,2,6,8]]],[[58,64],[[5,3,1,2,6,8]]],[[58,113],[[5,3,1,2,6,8]]],[[58,139],[[5,3,1,2,6,8]]],[[58,150],[[5,3,1,2,6,8]]],[[58,169],[[5,3,1,2,6,8]]],[[58,165],[[5,3,1,2,6,8]]],[[58,151],[[5,3,1,2,6,8]]],[[58,163],[[5,3,1,2,6,8]]],[[58,32],[[5,3,1,2,6,8]]],[[58,16],[[5,3,1,2,6,8]]],[[58,108],[[5,3,1,2,6,8]]],[[58,100],[[5,3,1,2,6,8]]],[[58,211],[[5,3,1,2,6,8]]],[[1,1],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,31],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,104],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,9],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,8],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,27],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,12],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,65],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,110],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,88],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,11],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,56],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,55],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,96],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,10],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,122],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,72],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,71],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,64],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,113],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,139],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,150],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,169],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,165],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,151],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,163],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,32],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,16],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,108],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,100],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[1,211],[[1,5,14,38,19,29,34,4,12,11,6,30,43,40,42,16,10,7]]],[[4,1],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,31],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,104],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,9],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,8],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,27],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,12],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,65],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,110],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,88],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,11],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,56],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,55],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,96],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,10],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,122],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,72],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,71],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,64],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,113],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,139],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,150],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,169],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,165],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,151],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,163],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,32],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,16],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,108],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,100],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[4,211],[[1,3,5,4,7,6,11,19,21,17,15,12,16,20]]],[[3,1],[[1,5,14,4,10,17]]],[[3,31],[[1,5,14,4,10,17]]],[[3,104],[[1,5,14,4,10,17]]],[[3,9],[[1,5,14,4,10,17]]],[[3,8],[[1,5,14,4,10,17]]],[[3,27],[[1,5,14,4,10,17]]],[[3,12],[[1,5,14,4,10,17]]],[[3,65],[[1,5,14,4,10,17]]],[[3,110],[[1,5,14,4,10,17]]],[[3,88],[[1,5,14,4,10,17]]],[[3,11],[[1,5,14,4,10,17]]],[[3,56],[[1,5,14,4,10,17]]],[[3,55],[[1,5,14,4,10,17]]],[[3,96],[[1,5,14,4,10,17]]],[[3,10],[[1,5,14,4,10,17]]],[[3,122],[[1,5,14,4,10,17]]],[[3,72],[[1,5,14,4,10,17]]],[[3,71],[[1,5,14,4,10,17]]],[[3,64],[[1,5,14,4,10,17]]],[[3,113],[[1,5,14,4,10,17]]],[[3,139],[[1,5,14,4,10,17]]],[[3,150],[[1,5,14,4,10,17]]],[[3,169],[[1,5,14,4,10,17]]],[[3,165],[[1,5,14,4,10,17]]],[[3,151],[[1,5,14,4,10,17]]],[[3,163],[[1,5,14,4,10,17]]],[[3,32],[[1,5,14,4,10,17]]],[[3,16],[[1,5,14,4,10,17]]],[[3,108],[[1,5,14,4,10,17]]],[[3,100],[[1,5,14,4,10,17]]],[[3,211],[[1,5,14,4,10,17]]],[[2,1],[[1,5,7,4,13,16,12,18]]],[[2,31],[[1,5,7,4,13,16,12,18]]],[[2,104],[[1,5,7,4,13,16,12,18]]],[[2,9],[[1,5,7,4,13,16,12,18]]],[[2,8],[[1,5,7,4,13,16,12,18]]],[[2,27],[[1,5,7,4,13,16,12,18]]],[[2,12],[[1,5,7,4,13,16,12,18]]],[[2,65],[[1,5,7,4,13,16,12,18]]],[[2,110],[[1,5,7,4,13,16,12,18]]],[[2,88],[[1,5,7,4,13,16,12,18]]],[[2,11],[[1,5,7,4,13,16,12,18]]],[[2,56],[[1,5,7,4,13,16,12,18]]],[[2,55],[[1,5,7,4,13,16,12,18]]],[[2,96],[[1,5,7,4,13,16,12,18]]],[[2,10],[[1,5,7,4,13,16,12,18]]],[[2,122],[[1,5,7,4,13,16,12,18]]],[[2,72],[[1,5,7,4,13,16,12,18]]],[[2,71],[[1,5,7,4,13,16,12,18]]],[[2,64],[[1,5,7,4,13,16,12,18]]],[[2,113],[[1,5,7,4,13,16,12,18]]],[[2,139],[[1,5,7,4,13,16,12,18]]],[[2,150],[[1,5,7,4,13,16,12,18]]],[[2,169],[[1,5,7,4,13,16,12,18]]],[[2,165],[[1,5,7,4,13,16,12,18]]],[[2,151],[[1,5,7,4,13,16,12,18]]],[[2,163],[[1,5,7,4,13,16,12,18]]],[[2,32],[[1,5,7,4,13,16,12,18]]],[[2,16],[[1,5,7,4,13,16,12,18]]],[[2,108],[[1,5,7,4,13,16,12,18]]],[[2,100],[[1,5,7,4,13,16,12,18]]],[[2,211],[[1,5,7,4,13,16,12,18]]]]]],None,None,[[[1,2],[10,8,9]]]],[query],1,[None,1],None,None,None,[True]],[True]]
    # fmt: on

    params['data'] = {'f.req': dumps([[["lGYRle", dumps(data), None, "3"]]])}

    return params


def response(resp):
    results = []

    res = loads(resp.text.splitlines()[2])[0][2]
    result_json = loads(res)

    if result_json[0][1] is None:
        return []

    for result in result_json[0][1][0][21][0]:
        try:
            content = result[13][1]
        except IndexError:
            content = ""

        results.append(
            {
                'url': urljoin('https://play.google.com', result[10][4][2]),
                'title': result[3],
                'content': html_to_text(content),
                'img_src': result[1][3][2],
            }
        )

    return results
