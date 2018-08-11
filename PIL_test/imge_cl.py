from PIL import Image
import os,re,pymql




work_dir = 'C:\\Users\\Administrator\\Desktop\\imge'
for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
    for filename in filenames:
        file_path = os.path.join(parent, filename)
        print('文件名：%s' % filename)
        print('文件完整路径：%s\n' % file_path)
        if  re.match("(.*?)g",filename):
            # 打开一个jpg或者png图像文件
            im = Image.open(file_path)
            # 获得图像尺寸:
            w, h = im.size
            # 缩放到50%:
            im.thumbnail((w/0.8, h/0.8))
            # 把缩放后的图像用jpeg格式保存:
            im.save(file_path, 'jpeg')
            # os.remove(file_path)

        else:
            print(">>>>>>>>>>文件%s不是图片："% filename,"<<<<<<<<<<\n")
