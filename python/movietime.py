#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 此程式是用來抓取離目前最近的該電影場次時間(格式僅為威秀電影院)
# 操作方式：./movietime.py 電影名稱
# 資料來源：http://www.vscinemas.com.tw/CinemaSessions.aspx?Lang=2
# PS: 請自行更換 urls 裡面的定義 {戲院名稱:威秀場次查詢url}

import sys
from HTMLParser import HTMLParser
import urllib

urls = {'新竹大遠百威秀':'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0005|HS&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode=', '新竹大遠百威秀 (Gold Class)':'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0005|HSGC&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode=', '新竹巨城威秀':'http://www.vscinemas.com.tw/visInternetTicketing3/visPrintShowTimes.aspx?visCinemaID=0012|BC&visMultiCinema=Y&visLang=2&ReturnURL=&visEventCode='}

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# 要帶一個電影名稱的參數
if len(sys.argv) < 2:
    print("usage: ./movietime.py moviename")
    exit()

moviename = sys.argv[1]

for (name, url) in urls.items():
    print(name+":")
    n_line = 0
    htmldata = strip_tags(urllib.urlopen(url).read())
    lines = htmldata.split("\n")
    for line in lines:
        if moviename in line:
            print(line.strip())
            print(lines[n_line+2].strip())
        n_line += 1

