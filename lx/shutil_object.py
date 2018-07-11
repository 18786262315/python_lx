
# 文件复制模块

import shutil


f1 = open('test1.txt','r')
f2 = open('test2.txt','w')

# shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
shutil.copyfileobj(f1,f2)
shutil.copyfile('test1.txt', 'test2.txt')