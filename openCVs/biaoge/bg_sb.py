import cv2
import numpy as np

def lk_mg(img_path):

    image1 = cv2.imread(img_path, 1)
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    #  findContours 获取轮廓
    contours, hierarchy = cv2.findContours(
        binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    content = []
    name = 0
    mean_size = np.mean([cv2.contourArea(i)for i in contours]) #获取平均面积
    for i, contour in enumerate(contours):
        size = cv2.contourArea(contour) #获取面积
        if 1 < size < mean_size: #大于平均面积的方块不获取
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image1, (x, y), (x + w, y + h), (146, 43, 33), 1)
            mb = {
            "width": "%s" % w,
            "height": "%s" % h,
            "left": "%s" % x,
            "top": "%s" % y,
            "name": "Rect%s" % name,
            "fill": "rgba(220,20,60,0.4)",
            "type": "rect"
            }
            content.append(mb)
            name += 1
    return content
