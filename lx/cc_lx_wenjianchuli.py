# tester:cc


import os

print(os.path.join('usr', 'bin', 'spam.txt')) #组合目录+文件

print(os.getcwd()) #当前目录

os.chdir('file_name')#切换工作目录

os.makedirs(os.path.join('D:', 'tt', 'name','lala')) #创建多层目录,不能跟文件名称。否则会被当作文件夹创建当文件夹存在时，会报错

print(os.path.abspath('.\\')) #返回参数的绝对路径，是将相对路径转换为绝对路径的简便方法

print(os.path.isabs('D:\\tt')) #如果参数是绝对路径就返回 True

os.path.relpath(path, start)#返回从start路径跳转到path的相对路径，如果没有start，就使用当前工作目录作为开始路径

print(os.path.dirname(os.getcwd()))#返回包含 path 参数中最后一个斜杠之前的所有内容，也叫目录名称





# f = open('test.txt','r+',encoding="utf-8")

# print (f.readline())# 读取一行文件
# print (f.tell())# 打印当前指针位置
# print (f.encoding)# 文件编码
# f.seek(0)# 移动指针
# print(f.readlines())#读取所有文件，已列表的形式读取
# f.write('cdasgdfs')
# f.flush()
# print(f.readlines())


