import numpy as np
import cv2

# Create a black image
img=np.zeros((1000,1000,3), np.uint8)


wt = [(367, 181), (459, 181), (367, 257), (459, 257),(400, 210), (500, 210), (400, 300), (500, 300)]
xiabiao = []
new_wt = []
cc = wt
for i in wt :
    for a in wt:
        if i[0] == a[0] and i[1] != a[1]:
            new_wt.append([i,a])
            cv2.line(img,i,a,(255,0,0),3)
            xiabiao.append(i[0]+i[1]+a[0]+a[1])
            print(i,a)
            print(i[0]+i[1]+a[0]+a[1])
        elif  i[1] == a[1]  and i[0] != a[0]:
            new_wt.append([i,a])
            xiabiao.append(i[0]+i[1]+a[0]+a[1])
            cv2.line(img,i,a,(255,0,0),3)
            print(i,a)
            print(i[0]+i[1]+a[0]+a[1])

print(new_wt)

# Draw a diagonal blue line with thickness of 5 px


# #draw rectangle
# cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# #draw circle
# cv2.circle(img,(447,63), 63, (0,0,255), -1)

# #draw ellipse
# cv2.ellipse(img,(256,256),(100,50),30,0,360,255,3)

# #draw multi-lines
# pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts=pts.reshape((-1,1,2))
# cv2.polylines(img,[pts],True,(0,0,255),3)#如果去掉中括号，只是画四个点

# #add words
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow('opencv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.waitKey(1)
# cv2.waitKey(1)
# cv2.waitKey(1)
# cv2.waitKey(1)
