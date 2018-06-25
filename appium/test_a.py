
# --*-- coding :utf-8 --*--

from appium import webdriver

def a_config():
  desired_caps = {
      "platformName": "Android",
      "platformVersion": "5.1.1",
      "deviceName": "127.0.0.1:21503",
      "appPackage": "com.mixgo.MixGo",
      "appActivity": "com.mixgo.ui.MixGoStartActivity"
      # 'unicodeKeyboard':True,
      # 'resetKeyboard':True
      }
  return desired_caps
  # 以下为启动driver，以及定位元素和操作元素的一些用例操作
def a_url():
  driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', a_config())
  return driver
