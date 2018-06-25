# -*- coding: utf-8 -*-
import unittest
from simulatemixgo import Login
from HTMLTestRunner import HTMLTestRunner
import time

class testLogin(unittest.TestCase):
    '''mixgo商家后台登录测试'''


    def setUp(self):
        print('开始单个测试')
        testLogin.login = Login()
    def tearDown(self):
        print('结束单个测试')
    def test_login1(self):
        '''mixgo商家后台登录测试'''
        self.login.login(username='13012345678',pw='123456')
        title=self.login.driver.title
        self.assertEqual(title,'MixGo商家开放后台')
        time.sleep(5)
        

if __name__=='__main__':
    unittest.main()