import numpy as np 
from matplotlib import pyplot as plt 
 


mylist = [1,2,2,2,2,3,3,3,4,4,4,4]

myset = set(mylist)  #myset是另外一个列表，里面的内容是mylist里面的无重复 项
counts = []
for item in myset:

  print("the %d has found %d" %(item,mylist.count(item)))
  counts.append(mylist.count(item))


# print(type(myset))
# x = np.arange(1,11) 
# y =  2  * x +  5 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.bar(list(myset),counts) 
plt.show()


