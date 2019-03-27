# import cv2
# import numpy as np
# import pytesseract

# image = cv2.imread(R'C:\Users\Administrator\Desktop\wben.jpg', 1)
# #二值化
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, -5)
# #ret,binary = cv2.threshold(~gray, 127, 255, cv2.THRESH_BINARY)
# cv2.imshow("cell", binary)
# cv2.waitKey(0)

# rows,cols=binary.shape
# scale = 40
# #识别横线
# kernel  = cv2.getStructuringElement(cv2.MORPH_RECT,(cols//scale,1))
# eroded = cv2.erode(binary,kernel,iterations = 1)
# #cv2.imshow("Eroded Image",eroded)
# dilatedcol = cv2.dilate(eroded,kernel,iterations = 1)
# # cv2.imshow("Dilated Image",dilatedcol)
# # cv2.waitKey(0)

# #识别竖线
# scale = 20
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(1,rows//scale))
# eroded = cv2.erode(binary,kernel,iterations = 1)
# dilatedrow = cv2.dilate(eroded,kernel,iterations = 1)
# # cv2.imshow("Dilated Image",dilatedrow)
# # cv2.waitKey(0)

# #标识交点
# bitwiseAnd = cv2.bitwise_and(dilatedcol,dilatedrow)
# # cv2.imshow("bitwiseAnd Image",bitwiseAnd)
# # cv2.waitKey(0)
# # cv2.imwrite("my.png",bitwiseAnd)

# #标识表格
# # merge = cv2.add(dilatedcol,dilatedrow)
# # cv2.imshow("add Image",merge)
# # cv2.waitKey(0)

# #识别黑白图中的白色点
# ys,xs = np.where(bitwiseAnd>0)
# mylisty=[]
# mylistx=[]

# #通过排序，获取跳变的x和y的值，说明是交点，否则交点会有好多像素值，我只取最后一点
# i = 0
# myxs=np.sort(xs)
# for i in range(len(myxs)-1):
#     if(myxs[i+1]-myxs[i]>60):
#         mylistx.append(myxs[i])
#     i=i+1
# mylistx.append(myxs[i])
# # print(mylistx)
# # print(len(mylistx))

# i = 0
# myys=np.sort(ys)
# #print(np.sort(ys))
# for i in range(len(myys)-1):
#     if(myys[i+1]-myys[i]>60):
#         mylisty.append(myys[i])
#     i=i+1
# mylisty.append(myys[i])
# # print(mylisty)
# # print(len(mylisty))

# i=0
# for i in range(4):  #只有4行有效数字
#     ROI = image[mylisty[i]:mylisty[i+1]-3,mylistx[1]:mylistx[2]-3] #减去3的原因是由于我缩小ROI范围
#     cv2.imshow("add Image",ROI)
#     cv2.waitKey(0)

#     special_char_list = '`~!@#$%^&*()-_=+[]{}|\\;:‘’，。《》/？ˇ'
#     pytesseract.pytesseract.tesseract_cmd = 'D://Program Files (x86)/Tesseract-OCR/tesseract.exe'
#     text2 = pytesseract.image_to_string(ROI)  #读取文字，此为默认英文
#     text2 = ''.join([char for char in text2 if char not in special_char_list])
#     print(text2)
#     i=i+1
# from PIL import Image
# from aip import AipImageClassify

# APP_ID = '15747543'
# API_KEY = 'IzjjdVQLMDBB2I9doYu6AujY'
# SECRET_KEY = '8KPWW7bnFGTdUILC3p327Gk2CuHFrqj4'

# client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

# def get_file_content(filePath):
#     with open(filePath, 'rb',) as fp:
#         return fp.read()


# nm = get_file_content(R'C:\Users\Administrator\Desktop\siteplan.jpg')
# ss = client.advancedGeneral(nm)
# print(ss)




import bisect
 
def binarySearch3(lst,x):
    i = bisect.bisect_left(lst,x)
    if i != len(lst) and lst[i] == x:
        return i
    raise RuntimeError('testError')
 
if __name__ == '__main__':
    lst = sorted([2,5,2,7,3,6,7,9,34,44])
    print (binarySearch3(lst,13))


# import bisect
# import random
 
# random.seed(1)
 
# print('New  Pos Contents')
# print('---  --- --------')
 
# l = []
# for i in range(1, 15):
#     r = random.randint(1, 100)
#     position = bisect.bisect(l, r)
#     bisect.insort(l, r)
#     print('%3d  %3d' % (r, position), l)