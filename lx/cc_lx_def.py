#!/usr/bin/python3
 

def count():
    fs = []
    for i in range(5):
        def f():
            return i*i
        fs.append(f())
    return fs

print (count())


class Person:
    "Person类"
    def __init__(self, name, age, gender):
        print('进入Person的初始化')
        self.name = name
        self.age = age
        self.gender = gender
        print('离开Person的初始化')
    def getName(self):
        print(self.name)
p = Person('ice', 18, '男')
print(p.name) # ice
print(p.age) # 18
print(p.gender) # 男
print(hasattr(p, 'weight')) # False
# 为p添加weight属性
p.weight = '70kg'
print(hasattr(p, 'weight')) # True
print(getattr(p, 'name')) # ice
print(p.__dict__) # {'age': 18, 'gender': '男', 'name': 'ice'}
print(Person.__name__) # Person
print(Person.__doc__) # Person类
print(Person.__dict__) # {'__doc__': 'Person类', '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__init__': <function Person.__init__ at 0x000000000284E950>, 'getName': <function Person.getName at 0x000000000284EA60>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__module__': '__main__'}
print(Person.__mro__) # (<class '__main__.Person'>, <class 'object'>)
print(Person.__bases__) # (<class 'object'>,)
print(Person.__module__) # __main__


for a in range(1,10):
    for b in range (1,10):
        c = a*b
        if b<=a:
               print (a,'x',b,'=',c,'\t',end='')

    print ()






def lazy_sum(*args):
    def sum():
        x=0
        for n in args:
            x=x+n
        return x
    return sum

lazy_sum(1,2,3,4,5,6,7,8,9) #这时候lazy_sum 并没有执行，而是返回一个指向求和的函数的函数名sum 的内存地址。
f=lazy_sum(1,2,3,4,5,6,7,8,9)
print(type(f))
print(f())  # 调用f()函数，才真正调用了 sum 函数进行求和，


def sum_s(*a):
    def sum():
        s = []
        for i in a:
            s.append('%s' % i)
        return s
    return sum

s = sum_s(4,6,5,7)

print (s())





#输出注解
def fun(): 
  """Some information of this function. 
  This is documentation string."""
  return
  
print(fun.__doc__) 



def fun(a, b, c=5): 
  print(a+b+c) 
  
fun(1,2) 
fun(1,2,3) 

def funt(a, L=[]): 
  L.append(a) 
  print(L) 
  
funt(1) # 输出[1] 
funt(2) # 输出[1, 2] 
funt(3) # 输出[1, 2, 3] 

def fib(): 
  """Print a Fibonacci series"""
  a, b = 0, 1
  c=[]
  while b < 2000:
      a, b = b, a+b
      if b%2 == 0: 
        c.append(b)
    
  return c

fib() # 当结果非单一字符串时，无法直接输出
print (fib())


#可写函数说明
f = lambda x, y: x+y 
print(f(10, 20)) 

s = lambda x,y,z:(x+y)*z

a = int(input("输入值一："))
b = int(input("输入值二："))
c = int(input('输入值三：'))
print ('结果：',s(a,b,c))
 
def make_fun(n): 
  return lambda x: x+n 
  
f = make_fun(15) 
print(f(5)) 



def test_return(x):
    #判断传入值是否大于5
    if x > 5:
        return '大于5'
    else:
        return '小于5'

print(test_return(9))

def s():
     '''
---------- 结束！！ -----------------


'''

print (s.__doc__)



