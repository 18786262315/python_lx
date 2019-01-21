from PIL import Image
# import os,re,pymql




# work_dir = 'C:\\Users\\Administrator\\Desktop\\imge'
# for parent, dirnames, filenames in os.walk(work_dir,  followlinks=True):
#     for filename in filenames:
#         file_path = os.path.join(parent, filename)
#         print('文件名：%s' % filename)
#         print('文件完整路径：%s\n' % file_path)
#         if  re.match("(.*?)g",filename):
#             # 打开一个jpg或者png图像文件
#             im = Image.open(file_path)
#             # 获得图像尺寸:
#             w, h = im.size
#             # 缩放到50%:
#             im.thumbnail((w/0.8, h/0.8))
#             # 把缩放后的图像用jpeg格式保存:
#             im.save(file_path, 'jpeg')
#             # os.remove(file_path)

#         else:
#             print(">>>>>>>>>>文件%s不是图片："% filename,"<<<<<<<<<<\n")


im = Image.open(R"F:\BaiduNetdiskDownload\世界著名城市风景建筑壁纸\世界著名城市风景建筑壁纸\城市壁纸 (14).jpg")
# print(im.format, im.size, im.mode)
# print(im.info)
# rgb2xyz = (0.412453,0.357580, 0.180423, 0,
#            0.212671,0.715160, 0.072169, 0,
#            0.019334,0.119193, 0.950227, 0 )
# new_im = im.convert('L',rgb2xyz)
# print(new_im.mode)
# new_im.show()
print(im.size)
box = (500, 0, 1280,1024)              ##确定拷贝区域大小
region = im.crop(box)                   ##将im表示的图片对象拷贝到region中，大小为box
region.show()
im.show()


