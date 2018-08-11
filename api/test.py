
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
import os,time,sched,re,smtplib,subprocess


new_filename = time.strftime("%y-%m-%d-%H-%M-%S", time.localtime())+".sql"
i_time =time.time()
# 如果是linux改下路径就可以了
cmdString = 'mysqldump -u root --password=ycc962464 ---all-databases > %s'%new_filename #备份语句
#执行备份语句并获取返回值；
# os.system(cmdString)
try:
    ret2 = subprocess.check_output(cmdString, shell=True)  
# obj = subprocess.Popen(cmdString, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# print()
# out_error_list = ret2.communicate()
# print(ret2)
except Exception as e:
    print(e)
    print(e)
    
    pass