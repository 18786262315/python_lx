# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from time import sleep
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.1"
caps["deviceName"] = "c76dc6fa"
caps["appPackage"] = "com.tencent.mm"
caps["appActivity"] = ".ui.LauncherUI"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

def loging():
        
    el1 = driver.find_element_by_id("com.tencent.mm:id/d37")
    el1.click()
    el2 = driver.find_element_by_id("com.tencent.mm:id/ht")
    el2.send_keys("18786262315")
    el3 = driver.find_element_by_id("com.tencent.mm:id/akb")
    el3.click()
    el4 = driver.find_element_by_id("com.tencent.mm:id/ht")
    el4.send_keys("daohao4nima..0")

    el5 = driver.find_element_by_id("com.tencent.mm:id/akb")
    el5.click()

    sleep(20)

sleep(10)    
el6 = driver.find_element_by_id("com.tencent.mm:id/ca5")
el6.click()
el7 = driver.find_element_by_accessibility_id('cc')
el7.click()
el8 = driver.find_element_by_id('com.tencent.mm:id/anc').click()

el9 = driver.find_element_by_id('com.tencent.mm:id/aac').send_keys('tester')
sleep(2)
el10 = driver.find_element_by_id('com.tencent.mm:id/aai').click()


driver.quit()