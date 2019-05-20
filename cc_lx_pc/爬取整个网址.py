import requests 
import re
import os
# import collections
import time
url_list =[] #创建一个列表用于储存已抓取的链接
lst2 = [] 
url =  'https://www.omega.im'
dyt = requests.get(url)
dyt
print(dyt)
r = 'href="(http:.*?|https:.*?)"'
dyt_url = re.findall(r,dyt.text) #提取当前页面的路径
print(dyt)
url_list.extend(dyt_url)# 将当前提取到的路径放到列表内
print(url_list)
# print(url_list)
def url_http(url):
    '''判断当前内容是否以http开头'''
    r1 = r'http://(.*)|https://(.*)'
    return re.match(r1,d_url)




while url_list: #循环列表
    d_url = url_list.pop(0) #提取列表的第一个元素
    if d_url !='' and d_url != '#': #判断路径是否合法
        
        if url_http(d_url) != None : #以http开头
            print('当前执行——————>'+d_url)
            t = requests.get(d_url).text #执行请求
            
        else:   #不以http开头时，进行拼接
            d_url = url+d_url
            d_url = re.sub(r'[a-z](//)',r'/',d_url) #
            print(d_url)
            t = requests.get(d_url).text #执行请求
            print('当前执行——————>'+d_url)
        r = 'href="(http:.*?|https:.*?)"'
        a = re.findall(r,t) #获取请求页面内的所有链接
        if 'page' in d_url: #判断请求是否包含下一页
            url_list.extend(a) #添加到列表  
            lst2.extend(a) #添加到列表  
            print(a)
        # print(a)
        lj = re.sub(r'http://|https://',r'/',d_url) #将包含http换成路径分隔符
        dr = 'C:\\Users\\Administrator\\Desktop\\a'+lj #合成路径
        n1 = re.sub(r'/',r'\\',dr) #修改路径分割符
        n = re.sub(r'\?(.*)|\#(.*)',r'',n1) #去除尾部参数
        mk = os.path.split(n) #文件名称与路径分割
        # print (mk)

        if r'\\' in mk[0]:
            continue

        elif mk[1] == '':
            continue

        elif os.path.exists(mk[0]) == True:

            with open (n,'w',encoding='utf-8') as f:
                f.write(t)
        else:
            if '\\n' in mk[0]:
                continue
            else:
                os.makedirs(mk[0])
                with open (n,'w',encoding='utf-8') as f:
                    f.write(t)




