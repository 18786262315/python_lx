import cv2
import numpy as np
import re
import requests
from urllib.parse import quote

imgs =  R"C:\Users\Administrator\Desktop\973715b109ce4a0e8eb53925468fc354.jpg"
urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"
l = 98 #最大宽度
n = 31#最大高度

image = cv2.imread(imgs, 1)
height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
# print("height:%s,width:%s,channels:%s" % (height, width, channels))
# print(image.size)
def dil2ero(img,selem):
    img=morphology.dilation(img,selem)
    imgres=morphology.erosion(img,selem)
    return imgres

# 二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, -1)
rows, cols = binary.shape
scale = 80

# 识别横线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols//scale, 1))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedcol = cv2.dilate(eroded, kernel, iterations=1)
cv2.imshow("add Image",dilatedcol)
cv2.waitKey(0)
# #识别竖线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows//scale))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedrow = cv2.dilate(eroded, kernel, iterations=1)
cv2.imshow("add Image",dilatedrow)
cv2.waitKey(0)
merge = cv2.add(dilatedcol,dilatedrow)
cv2.imshow("add Image",merge)
cv2.waitKey(0)

# 标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
jg = []
for x, hang in enumerate(bitwiseAnd):
    # 获取横向值
    if 255 in hang:
        for y, lie in enumerate(hang):
            # 获取竖向值
            for c, kuan in enumerate(hang):
                # 获取横向下一个点的值
                if c > y and kuan == 255:
                    e = 1
                    break
                e = 0
            for d, gao in enumerate(bitwiseAnd):
                # 获取竖向下一个点的值
                if d > x and gao[y] == 255:
                    f = 1
                    break
                f = 0
            if e == 1 and f == 1 and 2 <= int(c-y) <= l and 2 <= int(d-x) <= n:
                jg.append([[x, y], [(x, c), (d, y)]])
print('图片识别完成——————————>')
jieguo = []
name = 0
for i,keys in enumerate(jg):

    mb = {
        "width": "%s" % (int(keys[1][0][1])-int(keys[0][1])-2),
        "height": "%s" % (int(keys[1][1][0])-int(keys[0][0])-2),
        "left": "%s" % (keys[0][1]+1),
        "top": "%s" % (keys[0][0]+1),
        "name": "Rect%s" % (name),
        "fill": "rgba(220,20,60,0.4)",
        "type": "rect"
    }
    jieguo.append(mb)
    name += 1
# 推送到服务器
jieguo = re.sub("'", '"', '%s' % jieguo)  # 将单引号换成双引号
jieguo = re.sub("\n", '', '%s' % jieguo)  # 去除换行符
content = quote('%s' % jieguo, 'utf-8')  # 转码
payload = {"userId": "12",
           "token": "433bc525d0194606b2a030c446e1f526",
           "brokeId": "6b6c528605b445689fd8995cfe5f4f13",
           "sitePlanId": "671cdc6bdc464858915a5adc0b21e68c",
           "content": jieguo
           }
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls, data=payload)
print(ret)
