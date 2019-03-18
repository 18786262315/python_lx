import cv2
import numpy as np
from PIL import Image
import operator 


imgs =R'C:\Users\Administrator\Desktop\da.jpg'

image = cv2.imread(imgs, 1)
print(image[100,100])
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
print("height:%s,width:%s,channels:%s" % (height,width,channels))
print(image.size) 





#二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(~gray, 255, 
             cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -10)
# cv2.imshow("cell", binary)
# cv2.waitKey(0)

rows,cols=binary.shape
scale = 20
#识别横线
kernel  = cv2.getStructuringElement(cv2.MORPH_RECT,(cols//scale,1))
eroded = cv2.erode(binary,kernel,iterations = 1)
#cv2.imshow("Eroded Image",eroded)
dilatedcol = cv2.dilate(eroded,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedcol)
# cv2.waitKey(0)

# #识别竖线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,rows//scale))
eroded = cv2.erode(binary,kernel,iterations = 1)
dilatedrow = cv2.dilate(eroded,kernel,iterations = 1)
# cv2.imshow("Dilated Image",dilatedrow)
# cv2.waitKey(0)

#标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol,dilatedrow)

jieguo = []
for a,i in enumerate(bitwiseAnd):
    for m,t in enumerate(i):
        if t == 255:
            # print(i)
            jieguo.append((m,a))
            # print('----->',a,m)


print(jieguo)
xiabiao = []
new_wt = []
cc = jieguo
for i in jieguo :
    for a in jieguo:
        if i[0] == a[0] and i[1] != a[1]:
            new_wt.append([i,a])
            # cv2.line(image,i,a,(255,0,0),5)
            # xiabiao.append(i[0]+i[1]+a[0]+a[1])
            print(i,a,'---->',i[1]-a[1])
        elif  i[1] == a[1]  and i[0] != a[0] :
            new_wt.append([i,a])
            print(i,a,'---->',i[0]-a[0])
            # xiabiao.append(i[0]+i[1]+a[0]+a[1])
            # cv2.line(image,i,a,(255,0,0),3)
            # print(i,a)
            pass
#  and i[0]+i[1]+a[0]+a[1] not in xiabiao
print((new_wt))


print(jieguo)
print(bitwiseAnd.size)

cv2.imshow('opencv',image)
cv2.imshow("bitwiseAnd Image",bitwiseAnd)
cv2.waitKey(0)


# #标识表格
# merge = cv2.add(dilatedcol,dilatedrow)
# cv2.imshow("add Image",merge)
# cv2.waitKey(0)