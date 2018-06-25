# -*- coding: utf-8 -*-
from appium import webdriver
import test_config
from unittest import TestCase
from selenium.webdriver.common.by import By
import unittest
import time
import os

class MtcTest(TestCase):
    
    def setUp(self):
        config = test_config.get_test_config()
        uri = test_config.get_uri()
        self.driver = webdriver.Remote(uri, config)
        
    def test_login(self):
        # 在这里写自己的测试用例
        
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "测试")]').click()
        # time.sleep(10)
        
        self.swipe_percent(0.9, 0.5, 0.1, 0.5)
        time.sleep(1)
        self.swipe_percent(0.9, 0.5, 0.1, 0.5)
        time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/home_start").click()
        # time.sleep(1)
        # self.driver.find_element_by_id("com.test:id/btn_login").click()
        # time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/userName").click()
        # time.sleep(1)
        # self.enter_numbers("431381")        
        # time.sleep(1)

        # self.driver.find_element_by_id("com.test:id/password").click()
        # time.sleep(1)
        # self.enter_numbers("1234")       
        # time.sleep(1)
        
        # self.driver.find_element_by_id("com.test:id/btn_next_step").click()
        # time.sleep(5)
        
    def enter_numbers(self, number_str):
        for i in range(len(number_str)):
            self.driver.find_element_by_name(number_str[i]).click()

    def tearDown(self):
        self.driver.quit()

    def swipe_percent(self, percent_start_x, percent_start_y, percent_end_x, percent_end_y):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width * percent_start_x, height * percent_start_y, width * percent_end_x, height * percent_end_y)

if __name__ == '__main__':
  unittest.main()

