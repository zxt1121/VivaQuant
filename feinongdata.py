#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


Url = 'http://www.feinongdata.com/rili/'
myheaders = {'Content-Type': 'application/x-www-form-urlencoded',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
mydata = {'imp': '1', 't': time.strftime("%Y%m%d")}

def get_url():
    html = requests.post(Url, headers=myheaders, data=mydata)
    soup = BeautifulSoup(html.text, "lxml")
    i = 0
    for child in soup.tbody.children:
        a = re.compile(r'<td class="importantText nel"> (.*?)</td>')
        b = re.compile(r'<td align="center" rowspan="1">(.*?)</td>')
        c = re.compile(r'<span class="status-text">(.*?)</span>')
        d = re.compile(r'<td align="center" class="" id="tdzy"><img border="0" height="13" src="/app/Tpl/Index/Picture/(.*?).png" width="76"/></td>')
        name1 = a.findall(str(child))
        time1 = b.findall(str(child))
        trend1 = c.findall(str(child))
        importance1 = d.findall(str(child))
        for i1, x1 in enumerate(importance1):
            if int(x1)>=3:
                importance = x1
            for i2, x2 in enumerate(name1):
                name = x2
                for i3, x3 in enumerate(time1):
                    time = x3
                    for i4, x4 in enumerate(trend1):
                        trend = x4
                        i += 1
                        #return i, time, name, trend
                        print(i, time, name, trend)
def localtime():
    return time.strftime("%Y/%m/%d"), time.strftime("%H:%M:%S")

#if time.strftime("%H:%M")=='22:30':
start = time.time()
get_url()
end = time.time()
print(end-start)
print(localtime())