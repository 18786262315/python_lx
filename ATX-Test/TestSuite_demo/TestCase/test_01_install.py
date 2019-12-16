#!/usr/bin/env python
# -*- coding: utf-8 -*-

import uiautomator2 as u2
import time
import re
from Public.BasePage import BasePage
from Public.Decorator import *
from PageObject import login
import unittest
from Public.ReadConfig import ReadConfig

apk_url = ReadConfig().get_apk_url()
pkg_name = ReadConfig().get_pkg_name()
apk_path = ReadConfig().get_apk_path()


class apk_install(unittest.TestCase, BasePage):

    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_stop_all()

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.mixgo.PropertySEO")
 
    @setup
    def setUp(self):
        pass

    @teardown
    def tearDown(self):
        pass

    @testcase
    def test_stall_apk(self):
        '''安装启动com.mixgo.PropertySEO'''
        # self.d.app_uninstall(pkg_name)

        # self.d.app_install(apk_url)
        # self.local_install(apk_path)
        self.d.app_start(pkg_name)
        tanchuang = self.d(
            className="android.widget.LinearLayout", instance=1).wait(timeout=2)

        if tanchuang:
            # 判断是否有权限获取
            number1 = self.d(
                resourceId="com.android.packageinstaller:id/current_page_text").get_text()
            f = re.compile(r"\d+")
            number2 = f.findall(number1)[1]
            print(number2)
            for i in range(int(number2)):  # 循环点击每个权限获取
                self.d(
                    resourceId="com.android.packageinstaller:id/permission_allow_button").click()
        logins = self.d(text='ECOPROP').wait(timeout=2)
        if logins == False:
            self.d.click(302, 1292)  # 确认更新
            # self.d.click(783, 1281) #取消更新
            while logins != True:
                time.sleep(10)
                logins = self.d(text='ECOPROP').wait(timeout=2)

        # login.login_page().wait_page()

    @testcase
    def test_03_screenshot(self):
        '''手动截图测试'''
        self.screenshot()
        self.d.toast.show('HELLO ATX', 2)
        time.sleep(0.5)
        self.screenshot()

    @testcase
    def test_02_fail(self):
        '''异常处理'''
        ele = self.d(text='ECOPROP')
        print(ele.get_text())
        try:
            #  实际是 ECOPROP
            self.assertEqual(ele.get_text(), 'ECOPROP')
        except AssertionError:
            print('失败截图一张')
            raise
        finally:
            self.d(text='ECOPROP').click()
            print('手动截图一张')
            self.screenshot()

    # @testcase
    # def test_04_error(self):
    #     '''错误处理'''

    #     print('手动出错')
    #     raise Exception('手动ERROR!!!!!!!')
