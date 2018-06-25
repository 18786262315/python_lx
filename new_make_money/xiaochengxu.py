


# Python统计列表中的重复项出现的次数的方法



#方法1：

mylist = [1,2,2,2,2,3,3,3,4,4,4,4]

myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复 项

for item in myset:

  print("the %d has found %d" %(item,mylist.count(item)))



 

#方法2:

List=[1,2,2,2,2,3,3,3,4,4,4,4]

a = {}

for i in List:

  if List.count(i)>1:

    a[i] = List.count(i)

print (a)



 

"""利用字典的特性来实现。

方法3："""



from collections import Counter

Counter([1,2,2,2,2,3,3,3,4,4,4,4])

Counter({1: 5, 2: 3, 3: 2})







#方法4：只用列表实现的方法：



l=[1,4,2,4,2,2,5,2,6,3,3,6,3,6,6,3,3,3,7,8,9,8,7,0,7,1,2,4,7,8,9]

  

count_times = []

for i in l :

  count_times.append(l.count(i))

  

m = max(count_times)

n = l.index(m)

  

print (l[n])



#其实现原理就是把列表中的每一个数出现的次数在其对应的位置记录下来，然后用max求出出现次数最多的位置 







# 简单的拼手气红包

 

import random

from time import sleep

 

# 所有涉及金额的浮点数都需要用 round 方法保留2位小数，避免出现最终结果多出0.01

amount = round(float(input('请设置红包的金额 \> ')),2)

num = int(input('请设置红包的数量 \> '))

hb_dict = {}

xing = '赵钱孙李周吴郑王'

ming = '一二三四五六七八九十'

 

while num:

 

    xingming = random.choice(xing)+random.choice(ming)+random.choice(ming)

    if xingming in hb_dict.keys():

        xingming = random.choice(xing)+random.choice(ming)+random.choice(ming)

 

    num -= 1

    if num == 0:

        print('%s抢到红包%.2f元 红包抢完了!' % (xingming,amount))

        hb_dict[amount] = xingming

        amount -= amount

    elif num > 0:

        hb = round(random.uniform(0.01,amount)/num,2)

        hb_dict[hb] = xingming

        # 算法: 在0.01到红包总金额之间随机一个浮点数 / 红包剩余个数

        print('%s抢到红包%.2f元 剩余%d个!' % (xingming,hb,num))

        amount = round((amount - hb),2)

 

    sleep(1)

 

# 转置字典中的 key / value

# hb_dict2 = {value:key for key,value in hb_dict.items()}

max_hb = max(hb_dict.items())

print('%s运气最佳 抢得%.2f元!!' % (max_hb[1],max_hb[0]))



'''
mongodb基本操作及常用命令



查看已有的数据库,默认有个local

show dbs

查看已有的或集合,默认有个test

db

连接到指定的数据库,如果数据库不存在,则创建数据库

use easondb

往数据库easondb的集合mycol中插入一条数据 可以使用insert或save方法

db.mycol.insert({'id':1,'name':'Eason','age':25,'tags':['Linux','Python','MongoDB']})

db.mycol.save({'id':2,'name':'imaoxian','age':28,'tags':['C++','Java','javascript']})

查看集合中的数据,加上pretty()以结构化方式查看,也可以在find()中加入条件 符号对应关系 <:$lt <=:$lte >:$gt >=:ge !=:$ne

条件操作符详细教程:http://www.runoob.com/mongodb/mongodb-operators.html

db.mycol.find()

db.mycol.find().pretty()

db.mycol.find({'id':{$lte:2}})

根据条件查询

db.mycol.find({'id':2})

更新集合中的数据

db.mycol.update({'id':2},{$set:{'name':'Maoxian','age':29}})

删除集合中的数据

db.mycol.remove({'id':2})

删除集合

db.mycol.drop()

删除数据库

use easondb

db.dropDatabase()
'''


#python操作mongodb



import pymongo  # 导入pymongo模块

 

client = pymongo.MongoClient('127.0.0.1',27017)     # 创建一个mongo连接

db = client['testdb']                           # 定义一个名为testdb的 DB

sheet1 = testdb['sheet1']                       # 定义一个名为sheet1的 表

 

for i in range(100):

    # 循环生成一组词典

    data = {

        'i':i,

        'i*i':i*i

    }

    # 将词典insert到sheet1表中

    sheet1.insert_one(data)

 

# 读取出sheet1 中的数据

for item in sheet1.find():

    print(item) 



#python:pymysql数据库操作

import pymysql

 

# 获取一个数据库连接,注意如果是UTF-8类型的,需要制定数据库

db = pymysql.connect(host="127.0.0.1",user="root",passwd="123456",db="mysql",charset='utf8' )

# 使用 cursor()方法创建一个游标对象 cursor

cursor = db.cursor()

# 使用 execute()方法执行 SQL 查询

cursor.execute("SELECT user,host,password from user")

# 使用 fetchall()方法获取所有行.

data = cursor.fetchall()

print(data)

cursor.close()#关闭游标

db.close()#关闭数据库连接



import pymysql

 

db = pymysql.connect(host='10.3.1.174',user='root',password='123456',db='test')

cursor = db.cursor()

# SQL 插入数据

sql = "INSERT INTO employee (first_name, last_name, age, sex, income) " ,\
      "VALUES ('w', 'Eason', '29', 'M', '8000')"

# SQL 更新数据

# sql = "UPDATE employee first_name = Wang WHERE first_name = w"

# SQL 删除数据

# sql = "DELETE FROM employee WHERE age > 20"

 

try:

    cursor.execute(sql)

    db.commit()

except:

    db.rollback()

 

db.close()





随机生成200个序列号存入文件



import random

import string

 

for num in range(200):

    numlist = []

    for i in range(12):

        numlist.append(random.choice(string.ascii_uppercase+string.digits))

    # print(''.join(numlist))

    with open('200.txt', 'a') as f:     # 'a' 表示追加写入

        f.write(''.join(numlist)+'\n')













#写一个理财计算器，实现将每日/月/年的利息进行复投进行计算

 

money = float(input('请输入您打算用来投资的本金 \> '))

year = int(input('请输入投资期限(单位：年) \> '))

rate = float(input('请输入投资年化收益率 \> '))

Type = int(input('''1.每日利息复投 2.每月利息复投 3.每年利息复投

    请选择复投方式 \> '''))

 

def day_return(money,year,rate=0.12):

    '方案：每日利息加入本金复投！'

    for y in range(year):

        for day in range(365):

            money = money*rate/365 + money

        print('第%d年结束时，本金为：%.2f' % (y+1,money))

 

def month_return(money,year,rate=0.12):

    '方案：每月利息加入本金复投！'

    for y in range(year):

        for month in range(12):

            money = money*rate/12 + money

        print('第%d年结束时，本金为：%.2f' % (y+1,money))

 

def year_return(money,year,rate=0.12):

    '方案：每年利息加入本金复投！'

    for y in range(year):

        money = money*rate + money

        print('第%d年结束时，本金为：%.2f' % (y+1,money))

 

 

if Type == 1:

    day_return(money,year,rate)

elif Type == 2:

    month_return(money,year,rate)

elif Type == 3:

    year_return(money,year,rate)

else:

    print('输入有误！') 











#百度翻译

# Python 3.5.1

 

from urllib import request, parse

import json

 

url = 'http://fanyi.baidu.com/v2transapi'

context = input('请输入需要翻译的内容 :\> ')

 

if context >= '\u4e00' and context <= '\u9fa5':

    # 判断输入内容是否为汉字

    From,To = 'zh','en'

else:

    From,To = 'en','zh'

 

data = {

    'query':context,

    'from':From,

    'to':To,

    'transtype':'translang',

    'simple_means_flag':3

}

data = parse.urlencode(data).encode('utf-8')

 

r = request.Request(url,data)

r.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0')

html = request.urlopen(r).read().decode('utf-8')

Result = json.loads(html)

 

print('翻译结果为:' + Result['trans_result']['data'][0]['dst']) 



#python：乘法表





# for 循环

for i in range(1,10):

    for j in range(1,i+1):

        print('%dx%d=%d' % (j,i,j*i),end='\t')

    print()





# while 循环

m = 1

while m < 10:

    n = 1

    while n < m+1:

        print('%dx%d=%d' % (n,m,m*n),end='\t')

        n+=1

    m+=1

    print() 



生成激活码



#!/usr/bin/env python

#encoding:utf-8

#Author:sean

 

import string

import random

 

#激活码中的字符和数字

field = string.letters + string.digits

 

#获得四个字母和数字的随机组合

def getRandom():

    return ''.join(random.sample(field,4))

     

#生成的每个激活码中有几组

def concatenate(group):

    return '-'.join([getRandom() for i in range(group)])

     

#生成n组激活码

def generate(n):

    return [concatenate(4) for i in range(n)]

     

if __name__ == '__main__':

    print (generate(10))

#统计单词



#!/usr/bin/env python

#encoding:utf-8

 

import re

from collections import Counter

FileSource = './media/abc.txt'

 

def getMostCommonWord(articlefilesource):

    '''输入一个英文的纯文本文件，统计其中的单词出现的个数'''

    pattern = r'[A-Za-z]+|\$?\d+%?$'

    with open(articlefilesource) as f:

        r = re.findall(pattern,f.read())

        return Counter(r).most_common()

         

if __name__ == '__main__':

    print (getMostCommonWord(FileSource))

#提取网页正文



#!/usr/bin/env python

#encoding:utf-8

 

from goose import Goose

from goose.text import StopWordsChinese

import sys

 

#要分析的网页url

url = ''

 

def extract(url):

    '''

    提取网页正文

    '''

    g = Goose({'stopwords_class':StopWordsChinese}) 

    artlcle = g.extract(url=url)

    return artlcle.cleaned_text

 

if __name__ == '__main__':

    print (extract(url)) 



使用Python统计端口TCP连接数



import psutil

import prettytable

import time

 

startTime = time.time()

 

port = 22  # ssh -i /etc/ssh/ssh_host_rsa_key root@10.6.28.28

 

# define data structure for each connection, each ip is unique unit

ipaddress = {

    'ipaddress': None,

    'counts': 0,

    'stat': {

        'established': 0,

        'time_wait': 0,

        'others': 0

    }

}

 

# define data structure for statistics

statistics = {

    'portIsUsed': False,

    'portUsedCounts': 0,

    'portPeerList': [

        {

            'ipaddress': None,

            'counts': 0,

            'stat': {

                'established': 0,

                'time_wait': 0,

                'others': 0

            },

        },

    ]

}

 

tmp_portPeerList = list()

portPeerSet = set()

netstat = psutil.net_connections()

 

# get all ip address only for statistics data

for i, sconn in enumerate(netstat):

 

    if port in sconn.laddr:

        statistics['portIsUsed'] = True

        if len(sconn.raddr) != 0:

            statistics['portUsedCounts'] += 1

            ipaddress['ipaddress'] = sconn.raddr[0]

            tmp_portPeerList.append(str(ipaddress))  # dict() list() set() is unhashable type, collections.Counter

 

for ip in tmp_portPeerList:

    portPeerSet.add(str(ip))  # remove duplicated ip address using set()

 

for member in portPeerSet:

    statistics['portPeerList'].append(eval(member))

 

# add statistics data for each ip address

for sconn in netstat:

    if port in sconn.laddr:

        if len(sconn.raddr) != 0:

            for i, item in enumerate(statistics['portPeerList']):

                if item['ipaddress'] == sconn.raddr[0]:

                    statistics['portPeerList'][i]['counts'] += 1

                    if sconn.status == 'ESTABLISHED':

                        statistics['portPeerList'][i]['stat']['established'] += 1

                    elif sconn.status == 'TIME_WAIT':

                        statistics['portPeerList'][i]['stat']['time_wait'] += 1

                    else:

                        statistics['portPeerList'][i]['stat']['others'] += 1

 

# print statistics result using prettytable

if statistics['portIsUsed']:

    print ("Total connections of port %s is %d." % (port, statistics['portUsedCounts']))

    table = prettytable.PrettyTable()

    table.field_names = ["Total Counts", "Remote IP Address", "Established Conns", "Time_wait Conns",

                         "Others Conns"]

    for i, ip in enumerate(statistics['portPeerList']):

        if ip['ipaddress'] is not None:

            table.add_row([ip['counts'], ip['ipaddress'], ip['stat']['established'], ip['stat']['time_wait'],

                           ip['stat']['others']])

    print (table.get_string(sortby=table.field_names[1], reversesort=True))

else:

    print ('port %s has no connections, please make sure port is listen or in use.' % port)

 

endTime = time.time()

print ("Elapsed time: %s seconds." % (endTime - startTime) )



#python 收集主机信息



#!/usr/bin/env  python 

 

"""

file name: collect_info_a.py

"""

 

from  subprocess  import  Popen, PIPE

 

def  getIfconfig():

    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)

    data = p.stdout.read()

    return data

     

def  getDmi():

    p = Popen(['dmidecode'], stdout=PIPE, stderr=PIPE)

    data = p.stdout.read()

    return data

    

     

"""

从getIfconfig() 和getDmi() 函数返回的都是一个字符串。下面再定义一个

parseData(data) 的函数，将字符串分割成一个列表，每遇到顶格的行，就是

新的一段信息.

"""

def  parseData(data):

    parsed_data = []

    new_line = ''

    data = [i for i in data.split('\n')  if i] #将字符串分割，去掉空行的元素

    for  line  in data:

        if  line[0].strip():  #当遇到顶格的行，就把new_line 保存的上一段信息，append 到parsed_line

            parsed_data.append(new_line)

            new_line = line+'\n'  #重新保存新的一段的信息

        else:

            new_line += line+'\n'

    parsed_data.append(new_line)

    return [i for i in parsed_data if i]  #去掉空行的元素

    

    

     

"""

parseData(data) 函数返回的就是一个处理过的列表，将收集到的ip 字符串信息和 dmidecode 字符串信息，交给

下面定义的parseIfconfig() 和parseDmi() 函数分别处理，返回ip 信息的字典，和dmidecode 信息的字典。

"""

    

def  parseIfconfig(parsed_data):

    parsed_data = [i for parsed_data if i and  not i.startswith('lo')]  #将"lo" 网卡的信息去掉

    dic = {}

    for lines in parsed_data:

        devname = lines.split('\n')[0].split()[0]

        macaddr = lines.split('\n')[0].split()[-1]

        ipaddr  = lines.split('\n')[1].split()[1].split(':')[1]

        break   #由于只需要第一张网卡的信息，所以这里就可以退出循环了

    dic['ip'] = ipaddr

    return dic

     

def  parseDmi(parsed_data):

    dic = {}

    parsed_data = [i for i in parsed_data if  i.startswith('System Information')] #把这段信息直接整出来

    parsed_data = [i for i in parsed_data[0].split('\n')[1:] if i ]

    parsed_data = [i.strip().split(':') for i in parsed_data if i]

    dmi_dic = dict(parsed_data)

    dic = {}

    dic['vender'] = dmi_dic['Manufacturer'].strip()

    dic['product'] = dmi_dic['Product Name'].strip()

    dic['sn']  = dmi_dic['Serial Number'].strip()

    return dic

      

     

"""

getHostName: 函数

fn : 文件名参数

功能： 通过fn 传入文件名，读取HOSTNAME 信息

"""

def getHostName(fn):

    with open(fn) as fd:

        for line in fd:

            if line.startswith('HOSTNAME'):

                HostName = line.split('=')[1].strip()

                break

    return {'HostName': HostName}

     

     

"""

getOSver: 函数

fn : 文件名参数

功能： 打开fn　文件，读取操作系统版本信息

"""

def  getOSver(fn):

    with open(fn) as fd:

        for line in fd:

            osver = line.strip()

            break

    return {'osver': osver}

 

     

"""

getCpu: 函数

fn : 文件名参数

功能： 读取fn 文件信息，读取cpu 核数和cpu 型号

"""

def getCpu(fn):

    num = 0

    dic = {}

    with open(fn) as fd:

         for line in fd:

             if line.startswith('processor'):

                 num += 1

             if line.startswith('model name'):

                 model_name = line.split(':')[1]

                 model_name = model_name.split()[0] + ' ' + model_name.split()[-1]

    dic['cpu_num'] = num

    dic['cpu_model'] = model_name

    return dic

     

 

"""

getMemory: 函数

fn : 文件名参数

功能： 打开fn 文件，读取系统MemTotal 数值

"""

def  getMemory(fn):

    with open(fn) as fd:

        for line in fd:

            if line.startswith('MemTotal'):

                mem = int(line.split()[1].strip())

                break

    mem = '%s' % int((mem/1024.0)) +'M'

    return {'Memory': mem}

     

    

if  __name__ == '__main__':

    data_ip = getIfconfig()

    parsed_data_ip = parseData(data_ip)

    ip = parseIfconfig(parsed_data_ip)

     

    data_dmi = getDmi()

    parsed_data_dmi = parseData(data_dmi)

    dmi = prseDmi(parsed_data_dmi)

    HostName = getHostName('/etc/sysconfig/network')

    osver = getOSver('/etc/issue')

    cpu = getCpu('/proc/cpuinfo')

    mem = getMemory('/proc/meminfo')

    dic = {} #定义空字典，上面收集到的主机信息都是字典形式的，就是为了现在能将它们update 在一个字典

    dic.update(ip)

    dic.update(dmi)

    dic.update(HostName)

    dic.update(osver)

    dic.update(cpu)

    dic.update(mem)

    print dic



python 收集ip信息



#!/usr/bin/env  python

 

from subprocess  import  Popen, PIPE

 

def  getData():

    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)

    data = p.stdout.read().split（"\n\n"）

    return [i for i in data if i and  not  i.startswith('lo')]

     

def parseData(data):

    dic = {}

    for lines  in data :

        devname =  lines.split('\n')[0].split()[0]

        ipaddr =  lines.split('\n')[1].split()[1].split(':')[1]

        macaddr =  lines.split('\n')[0].split()[-1]

        dic[devname] = [ipaddr,  macaddr]

    return dic

     

     

if  __name__ == "__main__":

    data = getData()

    print parseData(data)





方法2：

#!/usr/bin/env  python 

 

from   subprocess  import   Popen, PIPE

 

def  getIP():

    p = Popen(['ifconfig'], stdout=PIPE, stderr=PIPE)

    stdout,  stderr  =  p.communicate()

    return  [i  for  i  in stdout.split('\n') if i]

         

def genIP(data):

    lines = []

    new_line = ''

    for line in data:

        if  line[0].strip():

            lines.append(new_line)

            new_line = line + '\n'

        else:

            new_line += line + '\n'

    lines.append(new_line)

    lines = [i for i in lines  if i and not i.starswith('lo')]

    return lines

     

     

def parseData(data):

    dic = {}

    for lines in data:

        devname = lines.split('\n')[0].split()[0]

        macaddr = lines.split('\n')[0].split()[-1]

        ipaddr  = lines.split('\n')[1].split()[1].split(':')[1]

        dic[devname] =  [ipaddr,  macaddr] 

    return dic   

     

if  __name__ == "__main__":

    data =  getIP()    

    data_list = genIP(data)

    print parseData(data_list)



python脚本： 双向统计文件字符、单词数、行数



#!/usr/bin/python



import sys

import os



if len(sys.argv) == 1:

        data = sys.stdin.read()

else:

        try:

                fn = sys.argv[1]

        except IndexError:

                print "please follow a argument at %s" %__file__

                sys.exit()



        if not os.path.exists(fn):

                print "%s is not exits." %fn

                sys.exit()





        fd = open(sys.argv[1])

        data = fd.read()



chars = len(data)

words = len(data.split())

lines = data.count('\n')



print "%(lines)s %(words)s %(chars)s" %locals()



python 代码统计文件的行数



#!/usr/bin/python

#encofing:utf8

# 统计文件的行数



import sys



def lineCount(fd):

        n = 0

        for i in fd:

                n += 1

        return n



fd = sys.stdin

print lineCount(fd)







python 递归法列出目录中的所有文件



用到的方法：

import os

os.listdir('/etc/')：列出指定目录下的所有文件和目录

os.path.isdir('/etc/')：判断是否是一个目录，返回一个布尔值

os.path.isfile('/etc/passwd')：判断是否是一个文件，返回一个布尔值

os.path.join('/etc','passwd')：连接两个路径

例：



#!/usr/bin/python



import sys

import os



def print_files(path):

    lsdir=os.listdir(path)

    dirs=[i for i in lsdir if os.path.isdir(os.path.join(path, i))]

    files=[i for i in lsdir if os.path.isfile(os.path.join(path, i))]

    if files:

        for f in files:

            print os.path.join(path, f)

    if dirs:

        for d in dirs:

            print_files(os.path.join(path, d))



print_files(sys.argv[1])







python 统计单词个数---不去重



import re

 

pattern  = re.compile(r'\w+')

 

pattern.match('hello ,world')

 

words = pattern.findall('hello hello  world')

 

len(words)



python 统计列表相同值重复次数





第一种：

    

    >>> test_list = ['a',0,'a',1,'a',0,1]

    >>> test_set = set(test_list)

    >>> for i in test_set:

    ...     print('values %s times %d' % (i,test_list.count(i)))

    ... 

    values a times 3

    values 0 times 2

    values 1 times 2



第二种：



    >>> from collections import Counter

    >>> test_list = ['a',0,'a',1,'a',0,1]

    >>> num = Counter(test_list)

    >>> num

    Counter({'a': 3, 0: 2, 1: 2})

    >>> num[0]

    2

    >>> num[1]

    2

    >>> num['a']

    3

    

第三种：

    >>> test_list = ['a',0,'a',1,'a',0,1,6]

    >>> test_dict = {}

    >>> for i in test_list:

    ...     if test_list.count(i) >= 1:

    ...             test_dict[i] = test_list.count(i)

    ... 

    >>> print(test_dict)

    {0: 2, 'a': 3, 6: 1, 1: 2}