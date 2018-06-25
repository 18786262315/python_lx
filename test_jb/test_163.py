# -*- coding: utf-8 -*-
import unittest
from simulate163 import Login
from HTMLTestRunner import HTMLTestRunner
import time

class testLogin(unittest.TestCase):
    '''163邮箱测试'''
    @classmethod
    def setUpClass(cls):
        print('开始测试')
        testLogin.login = Login()

    @classmethod
    def tearDownClass(cls):
        print('结束测试')
        testLogin.login.driver.quit()

    def setUp(self):
        print('开始单个测试')

    def test_login(self):
        '''163邮箱登录'''
        self.login.login(username='你的账号',pw='你的密码')
        title=self.login.driver.title
        self.assertEqual(title,'163网易免费邮--中文邮箱第一品牌')
        time.sleep(5)
    def test_logout(self):
        '''163邮箱退出登陆'''
        self.login.logout()
        title = self.login.driver.title
        self.assertEqual(title,'网易邮箱 - 您已成功退出邮箱')
        time.sleep(5)

    def tearDown(self):
        print('结束单个测试')

if __name__=='__main__':
    unittest.main()