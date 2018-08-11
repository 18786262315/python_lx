import shutil
import os
import os.path
 
#note:src's file unnecessary to be exist 
src="C:\\Users\\Administrator\\Desktop\\bq包\\file\\testFile_dst.txt"
dst = "C:\\Users\\Administrator\\Desktop\\bq包\\file\\testFile1_dst.txt"
dst2="C:\\Users\\Administrator\\Desktop\\bq包\\file\\testFile1_dst2.txt"
# shutil.copyfile(src, 'C:\\Users\\Administrator\\Desktop\\tester_work\\02\\')
def os_(file_,file2):
    ls = os.path.exists(file2)
    print(ls)
    if ls == False:
        print(os.makedirs(os.path.split(file2)[0]))
        
        shutil.copyfile(file_,file2)

    else:
        shutil.copyfile(file_,file2)
        pass


os_(src,'C:\\Users\\Administrator\\Desktop\\tester_work\\04\\03\\testFile_dst.txt')

# print(os.path.exists('C:\\Users\\Administrator\\Desktop\\tester_work\\02\\'))
# shutil.copytree('C:\\Users\\Administrator\\Desktop\\bq包\\file\\', 'C:\\Users\\Administrator\\Desktop\\tester_work\\02', ignore=shutil.ignore_patterns('testFile_dst.txt', 'tmp*'))
# print(os.path.split(src))
# print(os.path.split(src)[0])

