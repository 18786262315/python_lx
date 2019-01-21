import os 
import shutil
import numpy




print(numpy.msort([1,3,2,5,4,6,3]))



# # 批量复制图片
pd = "E:\\新联国际\\地产项目\\测试资料\\pingmiantu\\"

# def cp(pwd,name,number):
#     for i in range(number):
#         pwd1 = pwd+'\\'+name
#         pwd2 = pwd+'\\'+"D12-%s"%i+".png"
        
#         shutil.copy(pwd1,pwd2)


# cp(pd,"D12-01.jpg",100)

shutil.make_archive(pd,'zip',pd)