#usr/bin/python3
#! -*-conding : utf-8 -*-


#2018.3.14
"""
日历（Calendar）模块
此模块的函数都是日历相关的，例如打印某月的字符月历。
星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
"""
import time
import calendar

#calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
print(calendar.calendar(2018,w=2,l=1,c=6))

#calendar.firstweekday( ) 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
print (calendar.firstweekday())

# calendar.isleap(year) 是闰年返回True，否则为false。
print(calendar.isleap(2016))

# calendar.leapdays(y1,y2) 返回在Y1，Y2两年之间的闰年总数
print(calendar.leapdays(1999,2018))

# calendar.month(year,month,w=2,l=1) 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
print (calendar.month(2018,3,w=2,l=1))

# calendar.monthcalendar(year,month) 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
print(calendar.monthcalendar(2018,3,))

# calendar.monthrange(year,month) 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
print(calendar.monthrange(2018,4))

# calendar.prcal(year,w=2,l=1,c=6) 相当于 print calendar.calendar(year,w,l,c).

# calendar.prmonth(year,month,w=2,l=1) 相当于 print calendar.calendar（year，w，l，c）。

# calendar.setfirstweekday(weekday) 设置每周的起始日期码。0（星期一）到6（星期日）。
print (calendar.setfirstweekday(5))
print (calendar.month(2018,3,w=2,l=1))

# calendar.timegm(tupletime) 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
print (calendar.timegm(time.localtime()))

# calendar.weekday(year,month,day) 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）
print (calendar.weekday(2018,6,23))



#python中的calendar

#返回指定年的某月
def get_month(year, month):
    return calendar.month(year, month)

#返回指定年的日历
def get_calendar(year):
    return calendar.calendar(year)

#判断某一年是否为闰年，如果是，返回True，如果不是，则返回False
def is_leap(year):
    return calendar.isleap(year)

#返回某个月的weekday的第一天和这个月的所有天数
def get_month_range(year, month):
    return calendar.monthrange(year, month)

#返回某个月以每一周为元素的序列
def get_month_calendar(year, month):
    return calendar.monthcalendar(year, month)

def main():
    year = 2016
    month = 11
    test_month = get_month(year, month)
    print(test_month)
    print('#' * 50)
    #print(get_calendar(year))
    print('{0}这一年是否为闰年？：{1}'.format(year, is_leap(year)))
    print(get_month_range(year, month))
    print(get_month_calendar(year, month))

if __name__ == '__main__':
    main()




