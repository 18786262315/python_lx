
import operator 


wt = [(367, 181), (459, 181), (367, 257), (459, 257)]

for i in wt :
    for a in wt:
        if i[0] == a[0] or i[1] == a[1] :
            if operator.eq(a, i) :
                # print(operator.eq(a, i))
                pass
            elif i[0] != a[1] or i[1] != a[0]:
                print(i,a)

                # if i[0] == a[0]:
                #     print('宽')
                
                # else:
                #     print('高')


# {"width":"24","height":"11","left":"48","top":"283","name":"Rect0","fill":"rgba(220,20,60,0.4)","type":"rect"}





