# import os

# dr = os.popen("adb devices").read()  # 执行系统命令,并去读结果
# dl = list(dr)
# print (dl)

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from time import sleep
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "7.1.1"
caps["deviceName"] = "c76dc6fa"
caps["appPackage"] = "com.mixgo.MixGo"
caps["appActivity"] = "com.mixgo.ui.MixGoStartActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


#获取屏幕大小
def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


#屏幕向左滑动
print(getSize())


def swipLeft(t):
    l = getSize()
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    print(x1, y1, x2, y1)
    driver.swipe(x1, y1, x2, y1, t)


sleep(10)
swipLeft(1000)
sleep(5)
swipLeft(1000)

# TouchAction(driver).move_to(el=None,x=300, y=1330).release().perform()

# TouchAction(driver).press(x=856, y=1609).move_to(x=173, y=1660).release().perform()

TouchAction(driver).tap(x=536, y=1945).perform()


# print(self.driver.contexts)# 获取上下文列表
# cons = self.driver.contexts  #保存上下文
# self.driver.switch_to.context('WebView in com.tencent.tim')
# # self.driver.page_source
# print(self.driver.current_context)
# print(self.driver.page_source)

sleep(10)
el1 = driver.find_element_by_accessibility_id("pin 深圳市 ")
el1.click()
sleep(3)

el2 = driver.find_element_by_accessibility_id("arrow back ")
el2.click()
sleep(3)

TouchAction(driver).tap(x=533, y=50).perform()
TouchAction(driver).tap(x=606, y=1073).perform()
el3 = driver.find_element_by_xpath(
    "(//android.view.View[@content-desc=\"tab home 首页\"])[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]"
)
el3.click()
sleep(3)

TouchAction(driver).press(
    x=817, y=479).move_to(
        x=393, y=481).release().perform()

TouchAction(driver).press(
    x=876, y=520).move_to(
        x=410, y=533).release().perform()
sleep(3)

el4 = driver.find_element_by_xpath(
    "(//android.view.View[@content-desc=\"tab home 首页\"])[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[1]/android.view.View"
)
el4.click()
sleep(3)

el5 = driver.find_element_by_accessibility_id("arrow back ")
el5.click()
sleep(3)

el6 = driver.find_element_by_xpath(
    "(//android.view.View[@content-desc=\"tab home 首页\"])[2]/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]"
)
el6.click()
sleep(3)

el7 = driver.find_element_by_xpath(
    "//android.webkit.WebView[@content-desc=\"MixGo - 名家景选\"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]"
)
el7.click()
sleep(3)

el8 = driver.find_element_by_accessibility_id("show3d")
el8.click()

driver.quit()