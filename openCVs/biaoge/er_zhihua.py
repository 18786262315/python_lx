import cv2




def er_zhi(img_path):
    image = cv2.imread(img_path, 1)

    # 二值化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(
        ~gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,-1)
    rows, cols = binary.shape
    scale = 40
    # 识别横线
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cols//scale, 1))
    eroded = cv2.erode(binary, kernel, iterations=1)
    dilatedcol = cv2.dilate(eroded, kernel, iterations=1)
    # 识别竖线
    scale = 20
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, rows//scale))
    eroded1 = cv2.erode(binary, kernel, iterations=1)
    dilatedrow = cv2.dilate(eroded1, kernel, iterations=1)
    # 标识表格
    merge = cv2.add(dilatedcol, dilatedrow)
    imgs_pwd = R'new_img.jpg'
    # cv2.imshow("add Image",merge)
    # cv2.waitKey(0)
    cv2.imwrite(imgs_pwd, merge) # 将得到的表格图片储存
    return imgs_pwd