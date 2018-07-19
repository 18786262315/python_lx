#!usr/bin/python3
# -*- coding : utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

url = 'http://www.mixgo.com/biz/login?site=xishan'
url_quanxian = 'http://www.mixgo.com/biz/vendor/area?site=xishan'
url_shangping = 'http://www.mixgo.com/biz/vendor/offline?site=xishan'
# driver.manage().window().setSize(new Dimension(600, 400));
driver.set_window_size(597, 1078)
time.sleep(5)
driver.maximize_window()  # 最大化浏览器

phone = {
    '品牌商': '13012345678',
    #'品牌商直属员工':'18800000001',
    '大区经理': '15000000012',
    '代理商': '15000000001',
    '代理商店长': '18000000001',
    '代理商店员': '18700000001'
}

for i, s in phone.items():

    driver.get(url)
    driver.find_element_by_id('signin_name').send_keys(s)  #输入账号
    driver.find_element_by_id('signin_pass').send_keys('123456')  #输入密码
    driver.find_element_by_id('signin_btn').click()  #点击登录按钮

    #进入权限管理
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="sidebar-menu"]/div/ul/li[3]').click()
    # driver.get(url_quanxian)

    try:
        driver.find_element_by_link_text("大区管理").click()
        a = True
        print('成功进入权限管理', a)
    except:
        a = False
        print('未进入权限管理', a)

    #进入商品管理
    driver.find_element_by_xpath(
        '//*[@id="sidebar-menu"]/div/ul/li[2]/a').click()
    driver.find_element_by_xpath(
        '//*[@id="sidebar-menu"]/div/ul/li[2]/ul/li').click()

    driver.find_element_by_link_text("增加产品").click()

    driver.find_element_by_id('add-title').send_keys('ccc')

    driver.find_element_by_id('add-sku').send_keys("ss01 ")

    Select(driver.find_element_by_id('add-vendor')).select_by_visible_text(
        'MixGo')

    Select(driver.find_element_by_id('add-brand')).select_by_visible_text(
        'MixGo艺术品')

    Select(driver.find_element_by_class_name(
        'add-category')).select_by_visible_text("房产")

    file = driver.find_element_by_xpath('//*[@id="file_input1"]')
    file.send_keys("E:\\0001.jpg")
    # time.sleep(5)

    # driver.find_element_by_class_name('show').send_keys('E:\\0001.jpg')

    # driver.find_element_by_id('file_input2').send_keys('E:/0002.jpg')
    time.sleep(5)

    driver.find_element_by_xpath(
        "//*[@id='form-product']/div[13]/input[2]").click()
#driver.find_element_by_link_text('提交').click()

# # iframe有name或id值

# driver.switch_to.frame('iframe-name-id')

# # iframe没有name或id值

# xf = driver.find_element_by_xpath('//iframe[@allowtransparency="true"]')

# driver.switch_to.frame(xf)

# # 跳出当前iframe

# driver.switch_to.parent_content()

# # 返回最外层iframe

# driver.switch_to.default_content()

# driver.back()#返回上一层
#print ('当前账号是： %s'% i)

time.sleep(5)
print('结束本次测试')
driver.close()
