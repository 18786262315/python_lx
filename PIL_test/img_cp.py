from PIL import Image
import os
"""
WEBP 格式图片转换为JP格式图片

"""

img_pwd = "C:\\Users\\Administrator\\Desktop\\tp" #图片路径


files_list = os.listdir(img_pwd)

for files in files_list:
    
    if not os.path.isdir(files) and os.path.splitext(files)[1] == '.webp' :
        im = Image.open(img_pwd +'\\' + files)
        print('----WEBP格式文件')
        # im.load() # 读取图片像素信息
        background = Image.new("RGB",im.size,(255,255,255))
        background.paste(im,mask=im.split()[3])
        im = background
        im.save("%s.jpg"%(img_pwd +'\\' + files),"JPEG")

    else:
        print("---->这个文件不需要转换")





