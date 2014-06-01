#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib

# 新竹大遠百威秀
url = 'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0005|HS&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode='
print(urllib.urlopen(url).read())

# 新竹大遠百威秀 (Gold Class)
url = 'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0005|HSGC&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode='

# 巨城威秀
url = 'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0012|BC&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode='
