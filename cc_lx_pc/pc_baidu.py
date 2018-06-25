#!usr/bin/python3
# -*- coding:utf-8 -*-


import requests

import time



for m in range(0,2):

    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%A1%A8%E6%83%85%E5%8C%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%A1%A8%E6%83%85%E5%8C%85&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='+str(m*30)+'&rn=30&gsm=1e&1520500060263='

    html = requests.get(url)
    for n in range(30):
        
        demo = html.json()['data'][n]['middleURL']

        ss = requests.get(demo).content
        print(demo[-20:])

        with open('D:\\ycc\\pythonlianxi\\images\\'+demo[-20:-14]+'.jpg','wb') as f:

            f.write(ss)
   


# ss = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8E%86%E5%8F%B2')


