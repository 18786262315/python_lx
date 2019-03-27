import cv2
import requests
import re
import pytesseract
import numpy as np
from urllib.parse import quote
from PIL import Image
from aip import AipImageClassify

# 请求参数
urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"
userId = "15"
token="db4faa45c8d74316bf85e557bcb07339",
brokeId="ec40f23fb63640c680f1ff4789385016",
sitePlanId="37d87bb6ddbc4430bb099792b5232be2",

img_pth = R'C:\Users\Administrator\Desktop\de1aca6685aa4e9b8bd2608e9e381a07.jpg'

	
image = cv2.imread(img_pth, 1)
# 二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(
    ~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, -1)
rows, cols = binary.shape
scale = 20
# 识别横线
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols//scale, 1))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedcol = cv2.dilate(eroded, kernel, iterations=1)
# 识别竖线
scale = 10
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows//scale))
eroded1 = cv2.erode(binary, kernel, iterations=1)
dilatedrow = cv2.dilate(eroded1, kernel, iterations=1)
# 标识表格
merge = cv2.add(dilatedcol, dilatedrow)
cv2.imwrite(R'new_img.jpg', merge) # 将得到的表格图片储存
# cv2.imshow("add Image",merge)
# cv2.waitKey(0)

#获取交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
# cv2.imshow("add Image",bitwiseAnd)
# cv2.waitKey(0)
ys,xs = np.where(bitwiseAnd>0)
ll = [ (xs[i],ys[i]) for i in range(len(ys))] #获取交点)

# 二次处理
image1 = cv2.imread(R'new_img.jpg', 1)
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold( ~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#  findContours 获取轮廓
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

content = []
name = 0
mean_size = np.mean([cv2.contourArea(i)for i in contours]) #获取平均面积
f=0
for i, contour in enumerate(contours):
	x, y, w, h = cv2.boundingRect(contour)
	size = cv2.contourArea(contour) #获取面积
	for i in ll:
		if 0 <= int(x-i[0])<= 10 and 0 <= int(y-i[1])<= 10 :
			
			f = 1
			break
	if f !=0 and 1 < size < mean_size:

		x, y, w, h = cv2.boundingRect(contour)
		cv2.rectangle(image, (x, y), (x + w, y + h), (146, 43, 33), 1)

		mb = {
		"width": "%s" % (w-2),
		"height": "%s" % (h-2),
		"left": "%s" % (x+1),
		"top": "%s" % (y+1),
		"name": "Rect%s" % name,
		"fill": "rgba(220,20,60,0.4)",
		"type": "rect"
		}
		print(mb)
		content.append(mb)
		name += 1
	elif f == 0 :
		pass
		# print(y,y+w,x,x+w-w)

# 推送到服务器
content = re.sub("'", '"', '%s' % content)  # 将单引号换成双引号
content = re.sub("\n", '', '%s' % content)  # 去除换行符
# content = quote('%s' % content, 'utf-8')  # 转码
payload = {"userId": userId,
           "token": token,
           "brokeId": brokeId,
           "sitePlanId": sitePlanId,
           "content": content
           }
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls, data=payload)
print(ret.text)
