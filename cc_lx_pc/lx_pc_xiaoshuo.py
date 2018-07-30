#! usr/bin/python3
# -*- conding:gbk -*-

import requests
import re
import os

url = 'https://xiaoshuo.sogou.com/chapter/7619881134_249687923766147/'

ss = requests.get(url).text
print (ss)
#print (a)
zz = '<p>(.*?)</p>'
cc = re.findall(zz,ss)
vv= '&(.*?);'
ss = re.findall(vv,cc,re.S)
# print (cc)
print (ss)
for i in cc:
    with open("douban.txt","a") as f:

        f.write(i+'\n')
    
s = open ('douban.txt','r')

print (s.read())

s.close()














