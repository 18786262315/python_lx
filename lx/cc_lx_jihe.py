list_01 = [1,2,3,4,5,2,3,5,6,7]
list_01 = set(list_01)
print (list_01)
list_02 = set([9,3,23,54,65,5])
# 交集 
print (list_01.intersection(list_02))
print (list_01 & list_02)
#并集
print (list_01.union(list_02))
print (list_01 | list_02)
# 差集
print (list_01.difference(list_02))
print (list_01 - list_02)
#子集
print (list_01.issubset(list_02))
#父集
print (list_01.issuperset(list_02))
#对称差集，反向差集
print (list_01.symmetric_difference(list_02))
print (list_01 ^ list_02)

print (list_01.symmetric_difference_update(list_02))

# 判断交集
print (list_01.isdisjoint(list_02))








 


