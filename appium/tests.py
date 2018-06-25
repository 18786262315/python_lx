import os


dr = os.popen("adb devices").read()  # 执行系统命令,并去读结果
dl = list(dr)
print (dl)