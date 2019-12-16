#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject.home import home_page
from PageObject import login
from Public.Test_data import get_test_data
import unittest
from Public.Decorator import _create_gif





# @unittest.skip
class TestBootStrap(unittest.TestCase, BasePage):
    '''侧边栏检查'''

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_start("com.mixgo.PropertySEO")  # restart app
        cls.test_data = get_test_data(cls.d)

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.mixgo.PropertySEO")  # restart app
        # cls.set_original_ime()

    @setup
    def setUp(self):
        self.d.app_start("com.mixgo.PropertySEO")  # restart app
        logins = self.d(text=u'Loading').wait(timeout=2)
        while logins:
            # 加载页面 。
            time.sleep(5)
            logins = self.d(text='Loading').wait(timeout=2)
        self.d(className="android.widget.Image", instance=0).click()

    @teardown
    def tearDown(self):
        self.d.app_stop("com.mixgo.PropertySEO")  # restart app
        pass


    def loding(self):
        logins = self.d(text=u'Loading').wait(timeout=2)
        while logins:
            # 加载页面 。
            time.sleep(5)
            logins = self.d(text='Loading').wait(timeout=2)


    @testcase
    def test_01_emailsetting(self):
        '''Email Settings'''
        em_set = self.d(text=u"Email Settings")
        em_set.wait(timeout=2)
        em_set.click()

        self.d.toast.show('邮件设定页面', 2) # 弹窗
        self.screenshot()
        print('--------->>填写用户邮箱信息')
        #通过拍照添加头像，
        time.sleep(5)
        a = self.d(className="android.view.View", instance=16)
        a.wait(timeout=2)
        a.click()
        self.d(resourceId="android:id/icon").click()
        self.d(resourceId="com.huawei.camera:id/shutter_button").click()
        self.d(resourceId="com.huawei.camera:id/done_button").wait(timeout=2)
        self.d(resourceId="com.huawei.camera:id/done_button").click()
        self.screenshot()


        self.d(className="android.widget.EditText", instance=0).send_keys('ycc843092012@gmail.com')
        self.d(className="android.widget.EditText", instance=0).send_keys('个人介绍：\n 1、用户名称，\n 2、用户邮箱,\n 3、用户信息介绍')
        self.d.back()


    @testcase
    def test_02_Sent_Emails(self):
        '''Sent Emails'''
        print('------------->>>>>>>>')
        self.d(text=u"Sent Emails").click()

    @testcase
    def test_03_Password_Change(self):
        '''Password Change'''
        print('------------->>>>>>>>')
        self.d(text=u"Password Change").click()

    @testcase
    def test_04_Favorites(self):
        '''Favorites'''
        print('------------->>>>>>>>')
        self.d(text=u"Favorites").click()

    @testcase
    def test_05_My_Files(self):
        '''My Files'''
        print('------------->>>>>>>>')
        self.d(text=u"My Files").click()

    @testcase
    def test_06_Calendar(self):
        '''Calendar'''
        print('------------->>>>>>>>')
        self.d(text=u"Calendar").click()

    @testcase
    def test_07_Language(self):
        '''Language'''
        print('------------->>>>>>>>')
        self.d(text=u"Language").click()

    @testcase
    def test_08_Log_out(self):
        '''Log out'''
        print('------------->>>>>>>>')
        self.d(text=u"Log out").click()
