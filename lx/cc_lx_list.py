import copy

list1 = ['xiaozhi','aiweier','momo']
list2 = [1,2,3,4,5,6]
list3 = [[1,'iphone',8000],[2,'xiaoaitongxue',400]]

print (list3[1][0])
money = int(input('请输入你的工资：'))-1
print (money)
s = []
for i in list3:
    print (i)
    a = int(input('输入你要购买的商品编号：'))
    if a in list3.index(0):
        print(a)
#        print ()
    elif a == '':
        print('你没有输入商品''')
        a


