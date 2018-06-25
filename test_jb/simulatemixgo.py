'''
商家后台管理系统登录
'''
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Login():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.mixgo.com/biz/login?site=xishan")
    def login(self,username,pw):
        inputText=self.driver.find_element_by_id("signin_name")
        inputText.send_keys(username)
        password=self.driver.find_element(By.ID,"signin_pass")
        password.send_keys(pw)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.close()