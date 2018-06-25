
# -*- coding: utf-8 -*-
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
test_dir='./test_jb/'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

if __name__=='__main__':
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename=test_dir+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    runner.run(discover)
    fp.close()




    