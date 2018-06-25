class Cat:
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....%s"%self.san)

    def introduce(self):
        #print("%s的年龄是:%d"%(tom.name, tom.age))
        print("%s的年龄是:%d"%(self.name, self.age))



#创建一个对象
tom = Cat()

#调用tom指向的对象中的 方法
tom.san = 'weiwiew'
tom.age = 00
tom.eat()
tom.drink()


#给tom指向的对象添加2个属性
tom.name = "汤姆"
tom.age = 40

#获取属性的第1种方式
#print("%s的年龄是:%d"%(tom.name, tom.age))

tom.introduce()#相当于 tom.introduce(tom)


lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.introduce()
liuwei = Cat()
liuwei.name = 'ss'
liuwei.age = 90
liuwei.introduce()

s = ['a','b','c','d','e','f']

y = [1,3,5,6,7,8,9]

for i,n in zip(s,y):
            
        liuwei.name = i
        liuwei.age = n
        liuwei.introduce()
