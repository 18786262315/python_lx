#!usr/bin/python3
# -*- coding : utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'http://www.mixgo.com/biz/login?site=xishan'

driver.maximize_window()  # 最大化浏览器
phone = {
    '品牌商': '13012345678',
    '品牌商直属员工': '18800000001',
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

    time.sleep(5)
    # driver.back()#返回上一层
    print('当前账号是： %s' % i)

print('本次测试结束')
driver.close()

