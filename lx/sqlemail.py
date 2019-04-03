#!/usr/bin/python
# -*- coding: utf-8 -*-
"""数据库备份"""

import os, time, sched, re, subprocess, yagmail


# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数
# 第二个参数以某种人为的方式衡量时间


def backupsDB():
    """备份数据"""
    global new_filename
    try:
        print '---->1'
        new_filename = "/home/mixgo/sql/backup/mixgo_house_%s.sql"%time.strftime("%Y%m%d_%H",time.localtime()) #保存到当前脚本目录下。
        i_time = time.time()
        print '---->2'
        cmdString = 'mysqldump -u root --password=AUDAX88@ mixgo_house  > %s' % new_filename  #备份语句
        #执行备份语句并获取返回值；
        print '---->3'
        ret2 = subprocess.check_output(cmdString, shell=True)
        print '---->4'
        sendMail("备份成功%s"%ret2)
    except Exception as e:
        print '---->5%s'%e
        sendMail("备份失败%s"%e)

def sendMail(miss):
    print '---->6'
    yag = yagmail.SMTP(
        user="marketing@mixgo.com",
        password="mixgo88@",
        host='smtp.mxhichina.com')
    contents = "mixgo DB【mixgo_house】备份结果："+miss
    print '---->7'
    yag.send('1272769747@qq.com', 'mixgo_house DB备份', contents,[new_filename])
    print '--->8'


backupsDB()
