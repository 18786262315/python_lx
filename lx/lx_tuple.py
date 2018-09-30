from collections import namedtuple


#通过元组赋值的形式进行元组调用
car = namedtuple('car','name age color')
mycar = car('cc',12,'red')
print(mycar.name)

