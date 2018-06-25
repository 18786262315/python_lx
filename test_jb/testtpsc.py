#! usr/bin/python36
# -*- conding:utf-8 -*-

import os,sys


'''
for i in range(60):
    
    s = 18820000000+i
    #print (i)
    ss = open('D:\\ycc\\pythonlianxi\\test_jb\\test.txt','a')
        
    ss.writelines(str(s)+'\n')
    ss.close() 
'''


a = open('D:\\ycc\\pythonlianxi\\test_jb\\test.txt','r')

lines = a.readlines()

# for line in open('D:\\ycc\\pythonlianxi\\test_jb\\test.txt','r'):
#     print (line.strip())
for i in lines:
    print (i)

a.close() 