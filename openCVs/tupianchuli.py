import cv2
import numpy as np
import re
import requests
from urllib.parse import quote

imgs = R'C:\Users\Administrator\Desktop\siteplan.jpg'
urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"
l = 98 #最大宽度
n = 31#最大高度

image = cv2.imread(imgs, 1)



height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
# print("height:%s,width:%s,channels:%s" % (height, width, channels))
# print(image.size)


# 二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
rows, cols = binary.shape
scale = 20
# 识别横线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols//scale, 1))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedcol = cv2.dilate(eroded, kernel, iterations=1)

# #识别竖线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows//scale))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedrow = cv2.dilate(eroded, kernel, iterations=1)

# 标识交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
jg = []
# print(bitwiseAnd)
# print(bitwiseAnd.size)
for x, hang in enumerate(bitwiseAnd):
    # 获取横向值
    for y, lie in enumerate(hang):
        # 获取竖向值
        ll = []
        if lie == 255:
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
# print(jieguo)

# 推送到服务器
jieguo = re.sub("'", '"', '%s' % jieguo)  # 将单引号换成双引号
jieguo = re.sub("\n", '', '%s' % jieguo)  # 去除换行符
content = quote('%s' % jieguo, 'utf-8')  # 转码
payload = {"userId": "15",
           "token": "21e6778a17b64edcb40f9c1ca7ee42fa",
           "brokeId": "ec40f23fb63640c680f1ff4789385016",
           "sitePlanId": "9e06c416368946d095d05cb4f3ee1259",
           "content": jieguo
           }
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls, data=payload)
print(ret)
