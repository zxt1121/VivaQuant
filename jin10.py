# -*- coding:utf-8 -*-
import requests
import time
import json

myheaders = {'accept-language': 'zh-CN,zh;q=0.8',
             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

def web_get001():
    url = 'https://rili.jin10.com/datas/' + time.strftime("%Y") + '/'+ time.strftime("%m%d") +'/economics.json'
    try:
        rx= requests.get(url, headers=myheaders)  #获得网页,headers
    except:
        rx=None
        return None
    finally:
        return rx.text
    #
    return rx.text
starttime = time.time()
a = web_get001()
json_obj = json.loads(a)
for i,x in enumerate(json_obj):
    if json_obj[i]['star'] >= 3:
        print(json_obj[i]['publictime'], json_obj[i]['country'], json_obj[i]['dataname'], json_obj[i]['status_name'])
endtime = time.time()
print(endtime - starttime)