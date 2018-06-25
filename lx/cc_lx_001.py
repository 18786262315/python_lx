# #! usr/bin/python3.6

# # author : ycc

# import time 
# import os


for i in range(10):
    print(i)
    if i==5:
        break



# time_format = '%Y-%m-%d %X'

# time_s = time.strftime(time_format)
# print (time_s)

# def runt(s):
#     '''函数使用'''
#     s = s - 1
#     if s > 0:
#         print(s)
#         return runt(s)
#     else:
#        return 0 

# print(runt(5))



# c = ( i*2 for i in range(10000))

# # for i in c:
# #     print (i)
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())

# x = c.__next__()
# print('s',x)
# import time

# def fib(a):
#     s,x,y = 0,0,1
#     while s < a:
#         yield x
#         # print (y)
#         x,y = y,x+y
#         s= s+1

# f = fib(100) 
# #print (a.__next__())
# for i in f:
#     time.sleep(1)
#     print (f.__next__())

#!/usr/bin/python
# -*- coding: UTF-8 -*-


#天数计算 
# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))

# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0 < month <= 12:
# sum = months[month - 1]
# else:
# print ('data error')
# sum += day

# leap = 0 #www.iplaypy.com

# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
# leap = 1
# if (leap == 1) and (month > 2):
# sum += 1
# print ('it is the %dth day.' % sum)


# from appium import webdriver
# import time



# def id (value):
#     s = "driver.find_element_by_id(\"%s\").click()"% value
#     return s


# s = id("com.smartisanos.calculator:id/digit2")
# print (s)