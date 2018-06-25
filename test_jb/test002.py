#coding=utf-8 
   
from selenium import webdriver 
import time
   
driver = webdriver.Chrome() 
driver.maximize_window() 
driver.implicitly_wait(6) 
   
driver.get("https://www.baidu.com") 
driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
 
driver.back()
time.sleep(3)
 
driver.forward()
time.sleep(3)
 
ele_string = driver.find_element_by_xpath("//*[@id='1']/h3/a/em").text 
if (ele_string == "Selenium"): 

    print(driver.capabilities['version'])
 
driver.find_element_by_xpath("//*[@id='s_tab']/a[text()='新闻']").click() # 在搜索结果页面点击新闻类别 
 
time.sleep(1) 
 
print (driver.current_url)  # current_url 方法可以得到当前页面的URL 
print (driver.title)  # title方法可以获取当前页面的标题显示的字段 
 
driver.quit()