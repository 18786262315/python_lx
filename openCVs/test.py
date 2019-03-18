
import operator 
import numpy as np

wt = [(113, 170), (282, 170), (451, 170), (113, 212), (282, 212), (451, 212), (113, 254), (282, 254), (451, 254)]
(113, 170)

(113, 212)

(282, 170)

(282, 212)

for a1 in wt:
    b1= []
    for a2 in wt:
        if a1[0] == a2[0] or a1[1] == a2[1] :
            b1.append(a2)
    print(b1)





for x in wt:
    changfangx = []
    print(x)
    for y in wt:
        print('--->',y)
        if x[0] == y[0] and x[1] != y[1] and [y,x] not in changfangx  :
            changfangx.append([x,y])
            print('x----',x,y)
        elif  x[1] == y[1]  and x[0] != y[0] and [x,y] not in changfangx:
            changfangx.append([x,y])      
            print('y----',y,x)

        else:
            pass
    
    print(changfangx)







wt = np.array([(113, 170), (282, 170), (451, 170), (113, 212), (282, 212), (451, 212), (113, 254), (282, 254), (451, 254)])
xiabiao = []
new_wt = []

for i in wt :
    for a in wt:
        if i[0] == a[0] and i[1] != a[1] and [a,i] not in new_wt  :

            new_wt.append([i,a])
            xiabiao.append(i[0]+i[1]+a[0]+a[1])
            print(i,a,a[1]-i[1])
            
        elif  i[1] == a[1]  and i[0] != a[0] and [a,i] not in new_wt:
            new_wt.append([i,a])
            xiabiao.append(i[0]+i[1]+a[0]+a[1])
            print(i,a,a[0]-i[0])
            


print(new_wt)