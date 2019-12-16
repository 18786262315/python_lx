#!usr/bin/python3
# -*- coding:utf-8 -*-


import requests

import time



for m in range(0,2):

    url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%84%9F%E6%83%85%E7%94%B7%E5%A5%B3%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E6%84%9F%E6%83%85%E7%94%B7%E5%A5%B3%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1571035573221='
    html = requests.get(url)
    for n in range(len(html.json()['data'])-1):
        
        demo = html.json()['data'][n]['middleURL']

        ss = requests.get(demo).content

        print(demo[-20:])

        with open('E:\\ycc\\pythonlianxi\\images\\'+demo[-20:],'wb') as f:

            f.write(ss)
   


# ss = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E5%8E%86%E5%8F%B2')


