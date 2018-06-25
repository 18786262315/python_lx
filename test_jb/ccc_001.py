import os
import sys


#coding = gbk  
''''' 
#最终实现下面的过程 
foos = [1.0, 2.0, 3.0, 4.0, 5.0] 
bars = [100, 200, 300, 400, 500] 
 
1.0 [200, 300, 400, 500] 
2.0 [100, 300, 400, 500] 
3.0 [100, 200, 400, 500] 
4.0 [100, 200, 300, 500] 
5.0 [100, 200, 300, 400] 
#知识点 
1. map函数的理解 
2. 关键是切片函数的应用 
 

  
foos = [1.0, 2.0, 3.0, 4.0, 5.0]  
bars = [100, 200, 300, 400, 500]  
  
def func(foo):  
    index = foos.index(foo) #foo在foos中的索引，拿她取出来  
    print (foo,bars[:][0:index] + bars[:][index+1:])  
    #该索引同样在bars中相同位置，在切片的时候拿它取出，并拼接这个切片  
    #大功告成！  
  
print (map(func,foos) ) 

'''

''''' 
下面code.txt文件中内容，将 
01 CN Chinese 
02 IN India 
03 HK HongKang 
04 JP Japan 
05 DE Germany 
06 US United States of America 
要文件的内容，每一行文件，写到一个文件，且文件名前面两个字段，如 
文件名为:01_CN_Chinese.txt 
文中内容:01 CN Chinese 
知识要点: 
1. ''.join 和 split函数 
2. 字符的联合 
3. with语句,open文件 
4. 遍历数组 
5. 切片操作 
'''  
'''
print ('当前工作目录为 % s'% os.getcwd())
os.chdir('D:\\ycc\\pythonlianxi\\test_jb')
print ('当前工作目录为 % s'% os.getcwd())
postfix = '.txt'                     #设置后缀  

with open('test002.txt',) as s:
    for i in s:
        i= i.strip()
        print (i)
        for line in i:           #遍历列表  
            file_out = str('_'.join(line.split()[:])) + postfix #得到01_CN_Chinese.txt文件名  
            open(file_out,'w').write(line) 
'''

# with open('test.txt') as myfile:     #with语句打开文件为myfile  
#     while True:                      #while循环拿文件读出来  
#         lines = myfile.readlines()   #拿所有的行一次性读取到列表中  
#         if not lines: break          #没有则中断  
#         for line in lines:           #遍历列表  
#             file_out = str('_'.join(line.split()[:])) + postfix #得到01_CN_Chinese.txt文件名  
#             open(file_out,'w').write(line)   







print ('当前工作目录为 % s'% os.getcwd())
os.chdir('D:\\ycc\\pythonlianxi\\test_jb')
print ('当前工作目录为 % s'% os.getcwd())

f_r = open('test001.txt')  #打开要处理文件
f_c = open('test002.txt','w+')
f_w = open('file.txt','w') #创建要添加文件
a = []
s = 0
for a in f_c:
    s = s+1
    print (a)
    a= a.strip('\n')
    f_c.write(a+'str(s)'+'\n')
    # for s in f_r:
    #     f_w.write(a+s)

f_r.close()   #关闭打开的文件句柄
f_w.close()


'''
print ('当前工作目录为 % s'% os.getcwd())
os.chdir('D:\\ycc\\pythonlianxi\\test_jb')
print ('当前工作目录为 % s'% os.getcwd())
print(os.listdir(os.getcwd()))
ss = os.path.isfile('test.txt')
if ss == True :
    file1 = open('test.txt','r')
    list1 = []  #用一个空列表用于存放每行的内容  
    while True:  
        line = file1.readline()  
        list1.append(line.strip())  
        if len(line) == 0:  
            break  
    for l in list1[::-1]: #反向遍历，然后依次读取出来  
        print (l)  
    
    file1.close()  
else:
    print ('文件不存在')

'''


'''
#  反向读取内容：

list2 = ['shidf','fasdf','asdgaaa',123,45,6,45,3,1,4,]
print (list2[::-1])

for i in list2[::-1]:
    print (i)
'''