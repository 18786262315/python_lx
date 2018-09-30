# tester: cc

import re


#re.match()函数 #从字符串开始进行匹配
patter = 'pythonlalala'
r = 'python'
print(re.match(r,patter).group())
# r1 = 'lalala'
# print(re.match(r1,patter).group())

#re.search()函数 #全文检索匹配
r2 = 'lalala'
print(re.search(r2,patter).group())

# re.compile()函数 #预编译
patter1 = 'spythonlalalapythonlalalapythonlalala'
r3 = re.compile('.python.') #预编译
r4 = '.python.' #也可以不进行编译，具体会不会出问题，暂时没有遇到过
print(re.findall(r3,patter1)) 

#re.sub()函数 #字符串替换
string = "hellomypythonhispythonourpythonend"
pattern = "python."
print(re.sub(pattern,"php",string))  # 全部替换
print(re.sub(pattern,"php",string,2)) # 最多替换2次










