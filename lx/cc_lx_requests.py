# -*- coding : utf-8 -*-



import requests
import os,sys
import time
import json



urls = 'https://mp.weixin.qq.com/s/TCZSlaxeEEuvZpcfbfvmSA'
# f = open('test.txt','r')
# for line in f:
#     print (line.strip())
names = requests.get(urls)
print(names.text)
# url = "http://52.14.246.36/app/api/login?p=-1&userid=2&token=f61ad377add480aeb2b681ee371df93d&serial=7d6850664fe0c789a2101bfc7bca271e1282b29a&platform=x64&project=xishan&version=4&lang=zh-cn&modelver=2&country=1&appver=13&ip=&site=xishan&size=640x1136"
# for i in range(5):
#     for line in f :
#         line = line.strip()
#         print (line)
#         payload = {
#             'user_name': line,
#             'user_pass':'2b18917ff1d54dd77d56da5e27dd41e9'
#         }
#         headers = {'content-type': 'application/json'}

#         ret = requests.post(url, payload)
#         s = []
#         s = ret.text 
#         print (s)


    #print (ret.headers)


