
#! usr/bin/python3.6
# coding=utf-8  


# Python统计列表中的重复项出现的次数的方法




#方法2:

List=[1,2,2,2,2,3,3,3,4,4,4,4,5,5]

s = {}

for i in List:
    if List.count(i) >=1:
        s[i] = List.count(i)


print (s) 




a = {}

for i in List:

  if List.count(i)>1:

    a[i] = List.count(i)

print (a)


s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'


print (s.count)











"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import time


driver =webdriver.Chrome()

driver.get('http://52.14.246.36/biz/login?site=default')
driver.maximize_window()

#输入账号
driver.find_element_by_id('signin_name').send_keys('18786262315')

#输入密码
driver.find_element_by_id('signin_pass').send_keys('123456')

#点击登录按钮
driver.find_element_by_id('signin_btn').click()

time.sleep(3)

#展开产品管理下拉框：
#driver.find_element_by_xpath("//*[@id='sidebar-menu']/div/ul/li[2]/a").click()

time.sleep(3)

#点击产品上下架：

# #打开新窗口：
# newwindow = 'window.open("http://52.14.246.36/biz/brand_product_manage?site=default");'
# driver.execute_script(newwindow)
 
# # 切换到新的窗口
# handles = driver.window_handles
# driver.switch_to_window(handles[-1])
#进入到商品管理：

driver.get('http://52.14.246.36/biz/vendor/offline?site=default')

#点击新增商品：
# driver.find_element_by_class_name('input-group').click()


#点击MixGo艺术品：
Select(driver.find_element_by_id('filter-brand')).select_by_visible_text('MixGo艺术品')

#开始筛选：
driver.find_element_by_id('filter-btn').click()

#点击下一页
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div/div[4]/div/div[6]/ul/li[4]/a').click()



driver.current_url
time.sleep(3)


driver.close()
"""




