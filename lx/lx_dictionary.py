#!usr/bin/python3
# -*- conding : utf-8 -*-

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示


d = {'key1':'test001','key2':'test002','key3':10086}

print (d)
print (d['key2'])


#修改数据：
d['key3']=123
print (d['key3'])
#新增数据：
d['key4']='我是新增的'

#len()计算字典元素个数，就是键的总数
print(len(d))

#str()输出字典，以可以打印的字符串表示
print (str(d))

#type()返回输入的变量类型，如果变量是字典就返回字典类型。
print (type(d))


#del () 删除字典元素
del d['key1'] #单个删除
#print (d['key1'])
d.clear()#清空字典
del d    #删除字典


# 字典函数
# 1、radiansdict.clear() 删除字典内所有元素
dict = {'Name': 'Zara', 'Age': 7}
print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))

# 2、radiansdict.copy()返回一个字典的浅复制

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)

# 直接赋值与copy的区别
dict1 =  {'user':'runoob','num':[1,2,3]}
 
dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)
# 输出结果
print(dict1)
print(dict2)
print(dict3)


# 3、radiansdict.fromkeys()创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
#语法：dict.fromkeys(seq[, value]))
seq = ('name', 'age', 'sex')

dict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(dict))

dict = dict.fromkeys(seq, 13)
print ("新的字典为 : %s" %  str(dict))

dict['name']='小小'
print (str(dict))

#radiansdict.get(key, default=None)返回指定键的值，如果值不在字典中返回default值
'''
语法：dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
'''
dict = {'Name': 'Runoob', 'Age': 27}

print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))
print ('lianxi: %s'% dict.get('Name','liuhai'))

#key in dict如果键在字典dict里返回true，否则返回false
dict = {'Name': 'Runoob', 'Age': 7,'Sex':'女'}

# 检测键 Age 是否存在
if  'Age' in dict:
    print("键 Age 存在")
else :
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if  'Sex' in dict:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")

#radiansdict.items()以列表返回可遍历的(键, 值) 元组数组

dict = {'Name': 'Runoob', 'Age': 7}
dict['Sex']= '女'
dict['Age']=20
print ("Value : %s" %  dict.items())

#radiansdict.keys()以列表返回一个字典所有的键

dict = {'name':'ycc','age':26,'sex':'男'}
print ('我的名字叫：'+dict['name']+'\n''我今年 %a'% dict['age']+'岁''\n''我的性别是：%c'% dict['sex'])
print ('字典内的所有键值对为：%s' % dict.keys())

#radiansdict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
'''
语法：dict.setdefault(key, default=None)
参数：
key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
'''
print ("Age 键的值为 : %s" %  dict.setdefault('Age', '新的值'))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)

#adiansdict.update(dict2)把字典dict2的键/值对更新到dict里

dict = {'Name': 'Runoob', 'Age': 7}
dict2 = {'Sex': 'female' }
print ('更新之前的字典：',dict)
print (dict2)
dict.update(dict2)
print ("更新后的字典dict: ", dict)

#radiansdict.values()以列表返回字典中的所有值
dict = {'name':'小米','xiaoliang':30000,'leiji':300000,'jiage':'1000~5000'}
print ('字典内所有的值为：',list(dict.values()))

#pop(key[,default])删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)





















