

import sys
# import os
# # print(sys.path)
# print('c------c')
# # sys.argv[下标]#获取传入值

# if sys.argv[1] == str(1):
# 	print('这是一')
# if sys.argv[1] == str(2):
# 	print ('这是二')
# 	# cmd_res=os.system('dir')#执行命令，直接输出到屏幕上展示，不保存结果
# 	cmd_res=os.popen('dir').read()# 保存结果，不会直接输出到屏幕展示，当结果不read()的时候，读取到的是一个内存地址，必须要read()读取后才能正常展示
# 	print('cc-->',cmd_res)
# 	


# a,b,c=1,2,3

# d=a if a>b else c  #三元运算

# print(d)



# list

# name = ['zhangsan','lisi','wangwu']
# # 增加
# name.append('zhaoliu')#追加
# name.insert(1,'xiaoxiao')#插入指定位置
# print(name)
# name[1]='yugong'#替换
# print(name)
# 删除
# name.remove('yugong')# 删除指定值
# del name[1]#通过下标进行定位删除
# name.pop(4) #弹出指定下标
# print(name.index('lisi')) #查找下标
# print(name.count('zhangsan'))# 统计
# name.reverse()#反转列表
# name.sort()#排序

# name2=[1,2,3]
# name.extend(name2)#合并列表
# name.clear()#清空列表
# print(name)

#复制
# name1=name.copy()#浅cpoy 只复制一层列表


# enumerate() #获取列表下标

# for index,i in enumerate(name,1): # 从1开始计数，
# 	print(index,i)

# import sys


# def readfile(filename):  
#     try:  
#         f = open(filename)  
#         while True:  
#             line = f.readline()  
#             if not line:  
#                 break  
#             print (line)  
#     except:  
#         print ('some error here')  
  
# if len(sys.argv) < 2:  
#     print ('No action is needed!')  
#     sys.exit()  
  
# if sys.argv[1].startswith('--'):  
#     option = sys.argv[1][2:]  
#     if option in ['version','v','V','VERSION']:  
#         print ('Version 1.0')  
#     elif option in ['h','H','help','HELP']:  
#         print ("helpinfo")  
#     else:  
#         print ('Unknown option.')  
#     sys.exit()  
      
# else:  
#     for filename in sys.argv[1:]:  
#         readfile(filename)  

# import 

lists=['1','2','3','4','5']

# lists.pop(1)
# lists.pop().pop().pop().pop().pop()
# del lists[2] del lists[],del lists del del del del del del del 
# lists.remove('5').remove('').remove('').remove('')

print(lists.index('5'))
lists.reverse()
print(lists[::])
# print('-'.join(lists))

print(sys.getdefaultencoding()) #当前文件编码。



# def fib(max):
# 	n,a,b =0,0,1
# 	while n<max:
# 		# print(b)
# 		yield  b
# 		a,b =b, a+b
# 		n+=1
# 	return 'tester'

# a =fib(10)
# while True:
# 	try:
# 		x=next(a)
# 		print("a:",x) 
# 	except StopIteration as e:
# 		print ("最后一位：",e.value)
# 		break

# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


def consumer(name):
	print("%s 准备吃包子"% name)
	while True:
		baozi = yield
		print("包子[%s]来了,被[%s]吃了！！"%(baozi,name))
		

f = consumer("cc")
print(dir(f))
f.__next__() 

f.send("1")
f.send("2")
f.send("3")


# f.__next__()







