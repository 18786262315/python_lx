# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://mail.163.com/")

    def login(self, username, pw):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//*[@id='x-URS-iframe']")))
        self.driver.switch_to.frame("x-URS-iframe")
        inputText = self.driver.find_element(
            By.XPATH, "//*[@id='account-box']//div[2]//input")
        inputText.send_keys(username)
        password = self.driver.find_element(
            By.XPATH, "//*[@id='login-form']//div//div[3]//div[2]//input[2]")
        password.send_keys(pw).send_keys(Keys.ENTER)
        password

    def logout(self):
        self.driver.find_element_by_link_text('退出').click()
        time.sleep(5)