# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time






caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "9"
caps["deviceName"] = "3b710e8c"
caps["appPackage"] = "com.mixgo.PropertySEO"
caps["appActivity"] = "cn.jiguang.unity.push.UnityPluginActivity"
caps["noReset"] = "True"


driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

h = driver.get_window_size()['height']
w = driver.get_window_size()['width']
print(h,w)

# el1 = driver.find_element_by_id("com.qingqi.dianbo:id/btn_dynamic")
# el1.click()
# el2 = driver.find_element_by_id("com.qingqi.dianbo:id/iv_dynamic")
# el2.click()
# el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView[1]")
# el3.click()
# el4 = driver.find_element_by_id("com.qingqi.dianbo:id/left_btn")
# el4.click()
# el5 = driver.find_element_by_id("com.qingqi.dianbo:id/btn_dynamic")
# el5.click()
# el6 = driver.find_element_by_id("com.qingqi.dianbo:id/btn_ranlink")
# el6.click()
# el7 = driver.find_element_by_id("com.qingqi.dianbo:id/img_ranlink")
# el7.click()
# TouchAction(driver)   .press(x=479, y=1043)   .move_to(x=491, y=601)   .release()   .perform()
    
# TouchAction(driver)   .press(x=599, y=1998)   .move_to(x=555, y=1112)   .release()   .perform()
time.sleep(5)
    
# el8 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")
# el8.click()
# el9 = driver.find_element_by_id("com.qingqi.dianbo:id/tv_tab_new")
# el9.click()

# TouchAction.tap(x=403, y=2270).perform().release()
h = driver.get_window_size()['height']
w = driver.get_window_size()['width']
print(h,w)
TouchAction(driver).tap(x=403, y=2270).perform()
# TouchAction(driver).tap(x=400, y=2172).perform()
# TouchAction(driver).tap(x=66, y=125).perform()

driver.quit()