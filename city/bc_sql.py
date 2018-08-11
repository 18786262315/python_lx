#/usr/bin
# --*-- utf-8 --*--

import pymysql
import time
import re
import shutil
import os
# with open(js, encoding="utf-8") as f:
#     diqu = json.load(f)
db = pymysql.connect(host='localhost', user='root',
                        password='ycc962464', db='jingxuan')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

sql = "SELECT modelthumbs,modelpics,scanpic from mr_list a"

cursor.execute(sql)  # 执行sql语句


def copy_ (file_):
    file1 = "/home/wwwroot/default/"+file_ #原始文件夹
    file2 = '/root/'+file_ #要拷贝的文件夹
    ls1 = os.path.exists(file1)
    ls = os.path.exists(os.path.split(file2)[0])
    # print(ls)
    if file_ != '':#判断路径是否为空
        
        if ls == False or ls1 ==True: #判断路径不存在
            # print(os.path.split(file1)[0])
            os.makedirs(os.path.split(file2)[0])  #不存在则创建
            shutil.copyfile(file1,file2)
        else:
            shutil.copyfile(file1,file2) #存在则cp
            # print(os.path.split(file1)[0])
            pass
        print(os.path.split(file1)[1])

    else:
        pass

shujuku_name = cursor.fetchall()
for list_ in shujuku_name: 
    for lujing in list_ :
        if re.match('.*,',lujing):
            '''当一列存在多个路径时以逗号进行分割'''
            for lujing2 in lujing.split(','):
                # print(lujing)
                copy_(lujing2)
        else:
            copy_(lujing)





