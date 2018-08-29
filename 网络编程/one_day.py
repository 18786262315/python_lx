

class name(object):


    def __init__(self,name='not'):
        self.name = name
        self.__age = None
    
    # @staticmethod #静态方法，将函数和类分离
    # @classmethod #类方法，只允许访问类变量
    @property #attribute 属性方法，把一个方法变为一个静态属性。不能通过（）调用
    def wath(self):
        print('他的名字叫%s'%self.name,'今年：',self.__age)
    @wath.setter
    def wath(self,age):
        print('+1：',age)
        self.__age = age
    @wath.__delattr__
    def wath(self):
        del self.__age

n = name('小小')
n.wath
n.wath = 13

n.wath



























