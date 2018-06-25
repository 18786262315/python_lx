
from selenium import webdriver
from time import sleep


class Testmach():
  def __init__(self):
    self.driver=webdriver.Chrome()
    self.driver.driver.set_window_size(600,1078)
    self.driver.get('http://www.mixgo.com/app_v3')
    