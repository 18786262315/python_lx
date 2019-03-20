
import numpy as np
import cv2
img = cv2.imread( R'C:\Users\Administrator\Desktop\siteplan.jpg')
# 灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 阈值
_, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
# 膨胀
kernel = np.ones((3, 3), np.uint8)
dilated = cv2.dilate(threshold, kernel, iterations=1)
# 轮廓检测
contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 找到表格最外层轮廓
tree = hierarchy[0]
max_size = 0
outer_contour_index = None
for i, contour in enumerate(contours):
    size = cv2.contourArea(contour)
    if size > max_size:
        max_size = size
        outer_contour_index = i
contour = contours[outer_contour_index]
# 估算最小的单元格大小
x, y, w, h = cv2.boundingRect(contour)
cell_size = w * h * 0.0015
# 遍历所有最外层轮廓的子轮廓，过滤掉面积小于cell_size的，然后全部用矩形标注起来
contour_index = tree[outer_contour_index][2]
count = 0
while 1:
    contour = contours[contour_index]
    if cv2.contourArea(contour) > cell_size:
        x, y, w, h = cv2.boundingRect(contour)
        count += 1
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
    contour_index = tree[contour_index][0]
    if contour_index < 0:
        cv2.imwrite('11.jpg', img)
        break