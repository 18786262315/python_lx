import cv2
import numpy as np

imgs = R'C:\Users\Administrator\Desktop\siteplan.jpg'

image = cv2.imread(imgs)

print(image.shape)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
adaptive_binary = cv2.adaptiveThreshold(~gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
ret, thresh = cv2.threshold(adaptive_binary, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(image, contours, contourIdx, color, thickness)
cv2.imshow('aa',image)
cv2.waitKey(0)
