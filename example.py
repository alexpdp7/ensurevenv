#!/usr/bin/env python3
try:
    import ensurevenv
    ensurevenv.get(["requests", "beautifulsoup4"])
except Exception:
    pass


import bs4
import requests
import sys


print(bs4.BeautifulSoup(requests.get(sys.argv[1]).text).prettify())
