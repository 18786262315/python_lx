#usr/bin/python3


# print('\033[1;33;44mThis is a test !\033[0m')


import time 

import datetime
# 51test



s= ['20', '22', '07', '15', '14', '01', '18', '08', '10', '16', '12', '04', '03', '11', '00', '17', '21', '05', '23', '13', '19', '09', '06', '02']
s.sort()

print(s)

print(time.time()) # 获取当前时间戳

print(datetime.datetime.now()+datetime.timedelta(hours=-3))
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

print('----',time.localtime()) 
# time.sleep(2)
# print(time.clock()) 
# time.gmtime() # 转换当前时间，将当前时间转换为元组，以标准时区转换
print(time.gmtime(9000)) #将时间戳转换为元组形式 ,转换后的时间是，utc时间
print(time.localtime())#将当前时间转换成元组 ,本地时区。 
x = time.localtime()
print(x)
print('+-+-',time.mktime(x)) #将元组形式的时间转换为时间戳
time.strftime("%Y-%m-%d %H:%M:%S",x) #将元组格式的时间转换为格式化时间字符串表示。
s = time.strptime("2018-06-04 12:30:24","%Y-%m-%d %H:%M:%S")# %Y %m %d %H %M %S 时间表示格式
print(s)
print('111111')
print()
print()
print()


# import os

print(time.time())
print(time.localtime())
print(time.localtime())

#最简单的获取可读的时间模式的函数是asctime():
localtime = time.asctime(time.localtime(time.time()))
print ("本地时间为 :", localtime)

#python中时间日期格式化符号：
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
# # 格式化成2016-03-20 11:45:39形式
# print (time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))

# # 格式化成Sat Mar 28 22:24:24 2016形式
# print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
  
# # 将格式字符串转换为时间戳
a = "2019-11-29 15:30:21"
b = time.strptime(a,"%Y-%m-%d %H:%M:%S")
print(b)
print(time.strftime(" %H ",time.strptime(a,"%Y-%m-%d %H:%M:%S")))

# #time.altzone返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# print ("time.altzone %d " % time.altzone)

# #time.asctime([tupletime])接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# t = time.localtime()
# print ( "timr.asctime(t): %s" % time.asctime(t))

# #time.clock()用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
'''
def procedure():
    time.sleep(2.5)
# time.clock
t0 = time.clock()
procedure()
print (time.clock() - t0)
# time.time
t0 = time.time()
procedure()
print (time.time() - t0)
'''
# #time.ctime([secs])作用相当于asctime(localtime(secs))，未给参数相当于asctime() 传入的是时间戳
# print ("time.ctime() : %s" % time.ctime())

# #time.gmtime([secs])接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# print ('gmtime:',time.gmtime(1520999724.6782005))

# #time.localtime([secs]接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
# print ("localtime(): ", time.localtime(1455508609.34375))

# #time.mktime(tupletime)接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）
# #t-- 结构化的时间或者完整的9位元组元素。
# t = (2016, 2, 17, 17, 3, 38, 1, 48, 9)
# secs = time.mktime(t)
# print ("time.mktime(t) : %f" %  secs)
# print ("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))

# #time.sleep(secs)推迟调用线程的运行，secs指秒数。
# print ("Start : %s" % time.ctime())
# time.sleep( 5 )
# print ("End : %s" % time.ctime())
# #time.strftime(fmt[,tupletime])接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# #time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')根据fmt的格式把一个时间字符串解析为时间元组。
# struct_time = time.strptime("30 Nov 00", "%d %b %y")
# print ("返回元组: ", struct_time)

# #time.tzset()根据环境变量TZ重新初始化时间相关设置。
'''
标准TZ环境变量格式：std offset [dst [offset [,start[/time], end[/time]]]]

std 和 dst:三个或者多个时间的缩写字母。传递给 time.tzname.
offset: 距UTC的偏移，格式： [+|-]hh[:mm[:ss]] {h=0-23, m/s=0-59}。
start[/time], end[/time]: DST 开始生效时的日期。格式为 m.w.d — 代表日期的月份、周数和日期。w=1 指月份中的第一周，而 w=5 指月份的最后一周。'start' 和 'end' 可以是以下格式之一：
Jn: 儒略日 n (1 <= n <= 365)。闰年日（2月29）不计算在内。
n: 儒略日 (0 <= n <= 365)。 闰年日（2月29）计算在内
Mm.n.d: 日期的月份、周数和日期。w=1 指月份中的第一周，而 w=5 指月份的最后一周。
time:（可选）DST 开始生效时的时间（24 小时制）。默认值为 02:00（指定时区的本地时间）。

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))
 
os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print (time.strftime('%X %x %Z'))

'''




