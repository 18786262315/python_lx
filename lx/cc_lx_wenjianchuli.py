#!usr/bin/python
# -*- coding: utf-8 -*-

f = open('test.txt','r+',encoding="utf-8")

print (f.readline())# 读取一行文件
print (f.tell())# 打印当前指针位置
print (f.encoding)# 文件编码
f.seek(0)# 移动指针
print(f.readlines())#读取所有文件，已列表的形式读取
f.write('cdasgdfs')
f.flush()
print(f.readlines())


