# -*- coding : utf-8 -*-


import requests
import os
import sys
import time
import json
from urllib.parse import quote

urls = "http://api.singmap.com/broke-manager-service/siteplan/updateSiteContent"
# f = open("test.txt","r")
# for line in f:
#     print (line.strip())
# names = requests.get(urls)
# print(names.text)
# url = "http://52.14.246.36/app/api/login?p=-1&userid=2&token=f61ad377add480aeb2b681ee371df93d&serial=7d6850664fe0c789a2101bfc7bca271e1282b29a&platform=x64&project=xishan&version=4&lang=zh-cn&modelver=2&country=1&appver=13&ip=&site=xishan&size=640x1136"
# for i in range(5):
#     for line in f :
#         line = line.strip()
#         print (line)
#         payload = {
#             "user_name": line,
#             "user_pass":"2b18917ff1d54dd77d56da5e27dd41e9"
#         }
#         headers = {"content-type": "application/json"}

#         ret = requests.post(url, payload)
#         s = []
#         s = ret.text
#         print (s)

#print (ret.headers)
content = [{"width":"85","height":"24","left":"239","top":"341","name":"Rect0","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"86","height":"24","left":"239","top":"448","name":"Rect1","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"86","height":"24","left":"239","top":"1010","name":"Rect2","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"86","height":"24","left":"240","top":"1576","name":"Rect3","fill":"rgba(220,20,60,0.4)","type":"rect"}]
content = quote('%s'%content,'utf-8')
payload = {"userId": "6",
           "token": "54a408e0ffc048fb9f8591e038b4ae27",
           "brokeId": "0c5d80359cc5416a9ea953fdebcbfc20",
           "sitePlanId": "4e1f76d342fd48dcb1d20f7ae320ee8b",
           "content": content
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls,data=payload)
