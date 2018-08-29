
# # coding=utf-8 
# import sys 
# reload(sys) 
# sys.setdefaultencoding('utf-8') 
# from flask import Flask 
# import flask_restful 
# app = Flask(__name__) 
# api = flask_restful.Api(app) 
# class HelloWorld(flask_restful.Resource): 
# def get(self): 
#     return {'hello': 'world'} 
# api.add_resource(HelloWorld, '/') 
# if __name__ == '__main__': 
# app.run(host='0.0.0.0') 





# wl_list = ["1","2","3","4","5"]

# while wl_list:
#     s=0
#     print(wl_list[s])
#     if s>5:
#         s+=1
#     else:
#         s=0



# import time


# #循环生成器
# def traversal_list(alist, i):
#     while True:
#         length = len(alist)
#         i = i%(length)
#         yield alist[i]
#         i += 1

# def traversal_list2(alist):
#     i = 0
#     f = traversal_list(alist, i)
#     while True:
#         a = next(f)
#         print(a)
#         time.sleep(1)
#         i += 1

# if __name__ == '__main__':
#     alist = [1, 2, 3, 4, 5]
#     traversal_list2(alist)

# import time
# import datetime

# import os

# def TimeStampToTime(timestamp):
#     timeStruct = time.localtime(timestamp)
#     return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

# def get_FileCreateTime(filePath):
#     # filePath = unicode(filePath,'utf8')
#     t = os.path.getctime(filePath)
#     print(t)
#     return TimeStampToTime(t)

# print(get_FileCreateTime("E:\\ycc\\pythonlianxi\\18-08-07-15-45-53.sql"))
# import os,time,sched,re,smtplib,subprocess


# new_filename = time.strftime("%y-%m-%d-%H-%M-%S", time.localtime())+".sql"
# i_time =time.time()
# # 如果是linux改下路径就可以了
# cmdString = 'mysqldump -u root --password=ycc962464 ---all-databases > %s'%new_filename #备份语句
# #执行备份语句并获取返回值；
# # os.system(cmdString)
# try:
#     ret2 = subprocess.check_output(cmdString, shell=True)  
# # obj = subprocess.Popen(cmdString, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# # print()
# # out_error_list = ret2.communicate()
# # print(ret2)
# except Exception as e:
#     print(e)
#     print(e)
    
#     pass
# import pymysql

# db = pymysql.connect(host='192.168.254.130', user='root',
#                         password='ycc962464', db='pp_list')
# cursor = db.cursor()
# sql = "select * from user"

# cursor.execute(sql)  # 执行sql语句

# shujuku_name = cursor.fetchall()
# print (shujuku_name[0][1])
# # for i in shujuku_name[0]:
# #     print (i)





# import requests


# url = 'http://www.pmdaniu.com'
# api= {'_token':'rRa74Z7OjzPT978fegrKIoGPoNxYMMuCKhdEOjJ4',
#     'id':'23567',
#     'password':'1230'}
# enn = requests.post(url,data=api).text
# print (enn)
# r = requests.get('http://www.pmdaniu.com/cloud/23567/c853fcd10e4fc265cf40d72badb449fe-6568/start.html#&=&p=%E8%AE%BA%E8%AF%81%E6%B5%81%E7%A8%8B&g=1').text
# print(r)
# # print(requests.get('http://www.pmdaniu.com/cloud/23567/c853fcd10e4fc265cf40d72badb449fe-6568/start.html#g=1&p=%E8%AE%BA%E8%AF%81%E8%AF%A6%E6%83%85%E2%80%94%E5%BB%BA%E8%AE%BE%E5%8D%95%E4%BD%8Dpc').text)





import requests 
import re
import os
import collections
import time
# s=requests.Session()
param={'Host': 'www.pmdaniu.com',
'Connection': 'keep-alive',
'Content-Length': '70',
'Cache-Control': 'max-age=0',
'Origin': 'http://www.pmdaniu.com',
'Upgrade-Insecure-Requests': '1',
'Content-Type': 'application/x-www-form-urlencoded',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://www.pmdaniu.com/prototype/view?id=ACMGZ1E2ATECNQQ0ASkFdg',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'Hm_lvt_d642623fc3f6afb8c874ae3bfbbd8391=1534503961,1534819616; yx_auth=c853fcd10e4fc265cf40d72badb449fe; XSRF-TOKEN=eyJpdiI6Im9iVjIxd2dGOEpJS0wrUUlrcXNBS0E9PSIsInZhbHVlIjoiTms5aTVBeHUxQ29IdHA0NHltVjFYXC9JNjJ4XC82UVBYRmhTWER2OGVFRkM1NGZOZWRXNHpFcllPdVRDT2I1eFF1ZU9rSFNFWDFWSVNaZ2ptZWNmQkxrZz09IiwibWFjIjoiNDgyYzRhNTNhYTdmM2IyZjk3ZWMwYzY2OThjODExZTg1MDA0ZDljZjlhMWQ3NjU3ZmU2ZTcxZjQwOTlhZDFlMCJ9; daniu=eyJpdiI6ImliMzRmYUNMMTRId2pPeUNqa2lBRUE9PSIsInZhbHVlIjoiS2R0XC9iMjdnRDVMMkdKUmQ2SFBncXNXdzh1clZXKzhaUlFiMkZNYUVsMnZrQ256RERrazJGeGNEa0hHVXlwYWZFcGZBZEhDbFFvbjdHRlBUUzVJUWt3PT0iLCJtYWMiOiJjY2YxODgzZTJiMjM4YmEzZDhjZTNkMWQ4ZTFmZTVlNDQ3Mjk5ODJkODdmNDI4ZDAxYjVlYjYzZmZhMjA1MTk3In0%3D; Hm_lpvt_d642623fc3f6afb8c874ae3bfbbd8391=1534822140'
}
nn = {
'_token':'rRa74Z7OjzPT978fegrKIoGPoNxYMMuCKhdEOjJ4',
'id':'23567',
'password':'1230'
}
# url='http://www.pmdaniu.com/prototype/view'
# sx = requests.session()
# r=sx.post(url,headers=param,data=nn,verify=False)  #登录获取登录后的session
# # print(r.cookies)

# print(sx)
# for key,value in r.cookies.items():
#     print(key,'==',value,'-->')
# print(sx.get('http://www.pmdaniu.com/cloud/23567/c853fcd10e4fc265cf40d72badb449fe-6568/%E6%9E%B6%E6%9E%84%E5%9B%BEv1_0.html').text)



url_list =[]
url =  'http://www.pmdaniu.com/prototype/view/'
sx = requests.session()
r=sx.post(url,headers=param,data=nn,verify=False)
dyt = sx.get('http://www.pmdaniu.com/cloud/23567/c853fcd10e4fc265cf40d72badb449fe-6568/%E6%9E%B6%E6%9E%84%E5%9B%BEv1_0.html').text
r = 'href="(.*?)"'
dyt_url = re.findall(r,dyt) #提取当前页面的路径

url_list.extend(dyt_url)# 将当前提取到的路径放到列表内

# print(url_list)
def url_http(url):
    '''判断链接是否以http开头'''
    r1 = r'http://(.*)|https://(.*)'
    n = re.match(r1,d_url)
    if n == None:
        return True
    else:
        return False
while url_list: #循环列表
    d_url = url_list.pop(0) #提取列表的第一个元素
    if d_url !='' and d_url != '#': #判断路径是否合法
        
        if url_http(d_url) == False : #以http开头
            print('当前执行——————>'+d_url)
            t = sx.get(d_url).text #执行请求
            
        else:   #不以http开头时，进行拼接
            new_url = url+d_url
            new_url = re.sub(r'[a-z]//',r'/',new_url) #
            t = sx.get(new_url).text #执行请求
            print('当前执行——————>'+new_url)
        r = 'href="(.*?)"'
        a = re.findall(r,t) #获取请求页面内的所有链接
        url_list.extend(a) #添加到列表
        # print(a)
        lj = re.sub(r'http://|https://',r'/',d_url) #将包含http换成路径分隔符
        dr = 'C:\\Users\\Administrator\\Desktop\\a'+lj #合成路径
        n1 = re.sub(r'/',r'\\',dr) #修改路径分割符
        n = re.sub(r'\?(.*)|\#(.*)',r'',n1) #去除尾部参数
        mk = os.path.split(n) #路径分割
        print (mk)

        if r'\\' in mk[0]:
            pass

        elif mk[1] == '':
            continue

        elif os.path.exists(mk[0]) == True:

            with open (n,'w',encoding='utf-8') as f:
                f.write(t)
        else:
            if '\\n' in mk[0]:
                pass
            else:
                os.makedirs(mk[0])
                with open (n,'w',encoding='utf-8') as f:
                    f.write(t)












# http://www.pmdaniu.com/cloud/23567/c853fcd10e4fc265cf40d72badb449fe-6568/start.html