#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: liwen
'''
@time: 2018/8/6 9:19
'''
import os
import os.path

def clsriz():
    os.system("cls")  # 清楚日志
    print ("adb 启动中...")
    os.popen("adb devices")  # 执行命令
    os.system("cls")

def operation():
    result = os.popen('adb devices').readlines()  # os.popen()执行系统命令并返回执行后的信息对象
    n = len(result) - 2
    print (result)
    print ("检测到" + str(n) + "台设备：")
    devices = range(n)
    for i in range(n):
        nPos = result[i + 1].index("\t")
        devices[i] = result[i + 1][:nPos]
        print (str(i + 1) + " - " + devices[i])
    print (" ")
    nSel = 1
    if n != 1:
        nSel = input("选择设备：")
    if nSel <= n:
        dev = devices[nSel - 1]

    fn = raw_input("输入文件名：")
    fd = open(fn + '.cmd', 'w')

    if not os.path.isdir("D:\\" + fn):
        os.mkdir("D:\\" + fn)

    fd.write(":loop\n")
    fd.write("adb -s ")  # 选择设备
    fd.write(dev)  # 设备号
    fd.write(
        r" shell monkey  -p com.android.browser --monitor-native-crashes  --pct-touch 80 --pct-motion 15 --pct-nav 5 -s %random% -v  --throttle 500 320000 >d:\\")  # -s %random%的意思是防止产品相同的时间避免重复执行同一种动作
    fd.write(fn)
    fd.write("\\%random%.log\n")
    fd.write("@ping -n 15 127.1 >nul\n")  # ping自己15次用来延迟
    fd.write("adb -s ")
    fd.write(dev)
    fd.write(" reboot\n")
    fd.write("@ping -n 120 127.1 >nul\n")
    fd.write("@goto loop")

    fd.close()

    print ("批处理生成完毕")

if __name__ == '__main__':
    # clsriz()
    operation()