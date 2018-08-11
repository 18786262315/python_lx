
# import os,sys,subprocess

# # k = 'dir'
# cmdString = 'mysqldump -u root ---password=ycc962464 --all-databases > t1.py' #备份语句
# # result = os.popen("mysqldump -u root --password=ycc962464 --all-databases > \\t1.sql")
# res = subprocess.Popen(cmdString, shell=True)
# # res =result.readlines()
# # print(res.readlines())
# for line in res.splitlines():
#     print(line)
# #     # pass


# #用subprocess库获取返回值。
# p = subprocess.Popen(cmdString, shell=True, stdout=subprocess.PIPE)
# out, err = p.communicate()
# for line in out.splitlines():
#     print(line)


import subprocess
cmdString = 'mysqldump -u root --password=ycc962464 --all-databases > t1.py' #备份语句
# res1 = subprocess.Popen(cmdString)
# print(res1.())
obj = subprocess.Popen(cmdString, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out_error_list = obj.communicate(cmdString)
# print(out_error_list)
for l in out_error_list:
    if "ERROR" in out_error_list[1]:
        print(l)    


