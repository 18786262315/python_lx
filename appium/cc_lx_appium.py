from appium import webdriver
from appium.webdriver import Remote
from time import sleep
from selenium.webdriver.common.by import By
# 以下为启动session时的desired capabilities的设置


desired_caps = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.ximalaya.ting.android",
    "appActivity": "com.ximalaya.ting.android.host.activity.MainActivity"
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True

}
# 以下为启动driver，以及定位元素和操作元素的一些用例操作
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# driver.launch_app()


sleep(3)



kki = driver.page_source
driver.get_window_rect()
s = '不再提醒'
if s in kki:
    print('lalla')

else:
    print('ooo')


# driver.find_element(By.ID,"com.ximalaya.ting.android:id/cancel_btn").click()

# click_id('cancel_btn')
# def getSize(driver):
#     x = driver.get_window_size()['width']
#     y = driver.get_window_size()['height']
#     return (x, y)
# def swipeUp(driver,t=1000):
#     l = getSize(driver)
#     x1 = int(l[0] * 0.5)    #x坐标
#     y1 = int(l[1] * 0.75)   #起始y坐标
#     y2 = int(l[1] * 0.25)   #终点y坐标
#     driver.swipe(x1, y1, x1, y2,t)
# swipeUp(driver)
# swipeUp(driver)
# swipeUp(driver)
# swipeUp(driver)

# driver.tap([(96,53)])
# # driver.find_element_by_class_name('android.widget.FrameLayout')[0][1].send_keys('36氪')
# driver.keyevent(8)
# driver.keyevent(16)
# driver.keyevent(16)
# driver.keyevent(10)
# driver.tap([(645,202)])
# # driver.find_element_by_id("main_rl_search_suggest").click()

# click_id('main_fragment_playbar')
# sleep(3)
# driver.reset()

# # click_text("下次再说")


# # driver.find_element_by_id("com.ximalaya.ting.android:id/cancel_btn").click()


# print(driver.device_time)
# sleep(2)
# el1 = driver.find_element_by_id("cancel_btn")
# el2 = driver.find_element_by_id("main_tiv_cover")
# driver.drag_and_drop(el1[0],el2[0])

# # sleep(3)
# # driver.find_element_by_accessibility_id(u"搜索").click()
# # #点击搜索框

# # driver.keyevent(7)#0
# # driver.keyevent(8)#1
# # driver.keyevent(9)#2
# # driver.keyevent(10)#3
# # driver.keyevent(11)#4
# # driver.keyevent(12)#5
# # sleep(3)
# # driver.find_element_by_accessibility_id(u"下载").click()
# # driver.keyevent(4)#返回
# sleep(3)

# driver.close_app()
