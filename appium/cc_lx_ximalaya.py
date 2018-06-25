#coding:utf-8
#Import the common package
import os
import unittest
from appium import webdriver
from time import sleep

#设置路径信息
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        #初始化测试平台
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['app'] = 'D:\\apk\爱壁纸.apk'
        desired_caps['appPackage'] = 'com.lovebizhi.wallpaper'
        desired_caps['appActivity'] = '.Activity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        
      
    def tearDown(self):
       
        self.driver.quit()
        
    def test_1(self):
        #测试导航页
        print("start test1...")

        #判断是否安装爱壁纸APP
        wallpaper = self.driver.is_app_installed("com.lovebizhi.wallpaper")
        if wallpaper:
            #self.driver.remove_app("com.lovebizhi.wallpaper")
            sleep(8)
            # 点击某一壁纸图片
            self.driver.find_elements_by_id("com.lovebizhi.wallpaper:id/image1")[4].click()
            sleep(4)
            # 点击设置壁纸
            self.driver.find_element_by_id("com.lovebizhi.wallpaper:id/btSetup").click()
            sleep(5)
        else:
            self.driver.install_app("D:\\apk\\爱壁纸.apk")
            sleep(30)

    def test_2(self):
        #测试导航页
        print("start test2")

        #判断是否安装爱壁纸APP
        wallpaper = self.driver.is_app_installed("com.lovebizhi.wallpaper")
        #是
        if wallpaper:
            sleep(8)
            # 点击某一壁纸图片
            self.driver.find_elements_by_id("com.lovebizhi.wallpaper:id/image1")[5].click()
            sleep(4)
            # 点击设置壁纸
            self.driver.find_element_by_id("com.lovebizhi.wallpaper:id/btSetup").click()
            sleep(5)
        #否，安装
        else:
            self.driver.install_app("D:\\apk\\爱壁纸.apk")
            sleep(30)

                  

if __name__ == '__main__':
    suite =unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)