import cv2
import requests
import re
import pytesseract
import numpy as np
from urllib.parse import quote
from PIL import Image
from aip import AipImageClassify

# 请求参数
urls = "http://api.singmap.com/broke-manager-service/siteplan/updateSiteContent"
userId = "8"
token="1634e78d9dcf4b93958663177b78741d",
brokeId="56d272c6dfbb421da06664083d0607d1",
sitePlanId="3e987b4f77464105a82a977b28d70f38",

img_pth = R"E:\新联国际\地产项目\自动画图\HUATU\IMGS\ea96e1f62fa34f8da110e58daf8bfc2d.jpg"

	
image=cv2.imdecode(np.fromfile(img_pth,dtype=np.uint8),-1) # 中文路径问题解决

# 二值化
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("add Image",dilatedcol)
# cv2.waitKey(0)
binary = cv2.adaptiveThreshold(
    ~gray, 140, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,-1)
rows, cols = binary.shape
scale = 200

# 膨胀腐化
kernel = np.ones((2, 2), np.uint8)
# binary = cv2.dilate(binary, kernel) 
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel) 
# 识别横线




kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols//scale, 1))
eroded = cv2.erode(binary, kernel, iterations=1)
dilatedcol = cv2.dilate(eroded, kernel, iterations=1)
cv2.imshow("add Image",dilatedcol)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(
	dilatedcol, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,contours,-1,(0,0,255),2)
cv2.imshow("add Image", image)
cv2.waitKey(0)

# 识别竖线
# scale = 300
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows//scale))
eroded1 = cv2.erode(binary, kernel, iterations=1)
dilatedrow = cv2.dilate(eroded1, kernel, iterations=1)
cv2.imshow("add Image",dilatedrow)
cv2.waitKey(0)


# 标识表格
merge = cv2.add(dilatedcol, dilatedrow)
cv2.imwrite(R'new_img.jpg', merge) # 将得到的表格图片储存
cv2.imshow("add Image",merge)
cv2.waitKey(0)

#获取交点
bitwiseAnd = cv2.bitwise_and(dilatedcol, dilatedrow)
cv2.imshow("add Image",bitwiseAnd)
cv2.waitKey(0)
ys,xs = np.where(bitwiseAnd>0)
ll = [ (xs[i],ys[i]) for i in range(len(ys))] #获取交点)

# 二次处理
image1 = cv2.imread(R'new_img.jpg', 1)
cv2.imshow("add Image", image1)
cv2.waitKey(0)
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold( ~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, -1)
ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#  findContours 获取轮廓

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image1,contours,-1,(0,0,255),2)

cv2.imshow("add Image", image1)
cv2.waitKey(0)
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
	if f !=0 and 10 < size < mean_size:

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

# # 推送到服务器
# content = re.sub("'", '"', '%s' % content)  # 将单引号换成双引号
# content = re.sub("\n", '', '%s' % content)  # 去除换行符
# # content = quote('%s' % content, 'utf-8')  # 转码
# payload = {"userId": userId,
#            "token": token,

		   
#            "brokeId": brokeId,
#            "sitePlanId": sitePlanId,
#            "content": content
#            }
# headers = {"Content-Type": "application/x-www-form-urlencoded"}
# ret = requests.post(urls, data=payload)
# print(ret.text)
