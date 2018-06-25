#!usr/bin/python3
# -*- coding : utf-8 -*-



from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
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

#点击找回密码按钮
driver.find_element_by_class_name('toforget').click()

#找回密码界面-手机号码输入框：
driver.find_element_by_id('reset_name').send_keys('18786262315')

#找回密码界面-验证码输入框:
driver.find_element_by_id('reset_verify').send_keys('****')

#找回密码界面-密码输入框：
driver.find_element_by_id('reset_pass_1').sned_keys('123456')

#找回密码界面-确认密码输入框：
driver.find_element_by_id('reset_pass_2').send_keys('123456')

#修改密码界面-确认修改按钮：
driver.find_element_by_id('reset_btn').click()

#点击MixGo官网按钮：
driver.find_element_by_xpath('/html/body/div/div[1]/h4[1]/a').click()

#点击APP产品按钮：
driver.find_element_by_xpath('/html/body/div/div[1]/h4[2]/a').click()

#点击首页：
driver.find_element_by_class_name('current-page').click()

#展开产品管理下拉框：
driver.find_element_by_class_name('fa fa-chevron-down').click()

#点击产品上下架：
driver.find_element_by_class_name('nav child_menu').click()

#点击权限管理按钮：
driver.find_element_by_class_name('current-page').click()

#点击新增产品：
driver.find_element_by_class_name('btn btn-success').click()

#点击等待审核：
driver.find_element_by_class_name('col-lg-2 col-md-2 col-sm-4 col-xs-6 col-lg-offset-1 col-md-offset-1 col-sm-offset-2 active').click()

#点击审核通过：
driver.find_element_by_class_name('col-lg-2 col-md-2 col-sm-4 col-xs-6').click()

#条件筛选栏：
#关键字输入框：
driver.find_element_by_id('filter-key').send_keys(u'查询字段')

#品牌选择下拉框：
driver.find_element_by_id('filter-vendor').click()
#品牌选择：
driver.find_element_by_xpath("//*[@id='filter-vendor']/option[列表值]").click()

#系列选择下拉框：
driver.find_element_by_id('filter-brand').click()
#系列选择：
driver.find_element_by_xpath('//*[@id="filter-brand"]/option[列表值]').click()

#空间选择下拉框：
driver.find_element_by_id('filter-space').click()
#空间选择：
driver.find_element_by_xpath('//*[@id="filter-space"]/option[列表值]').click()

#风格选择下拉框：
driver.find_element_by_id('filter-style').click()
#风格选择：
driver.find_element_by_xpath('//*[@id="filter-style"]/option[列表值]').click()

#分类选择下拉框：
driver.find_element_by_class_name('form-control filter-category').click()

#已查询到的商品数量：
s = driver.find_element_by_class_name('hidden-xs').text
print (s)

#清空已选择的条件：
driver.find_element_by_id('filter-clear').click()

#开始筛选：
driver.find_element_by_id('filter-btn').click()

#每页展示数量下拉选择框：
driver.find_element_by_id('filter-num').click()
#每页数量选择：10/20/50/200/500
driver.find_element_by_class_name('//*[@id="filter-num"]/option[1]').click()

#排序规则下拉框：
driver.find_element_by_id('filter-sort').click()
#排序规则选择：
driver.find_element_by_xpath("//*[@id='filter-sort']/option[1]").click()

#分类选择下拉框：
driver.find_element_by_id('').click()
#分类选择：
driver.find_element_by_xpath("//*[@id='category-container']/select/option[2]").click()


#等待审核商品操作：
#1、编辑商品：
driver.find_element_by_class_name('btn btn-info').click()
#2、删除商品：
driver.find_element_by_class_name('btn btn-danger product_del').click()
#3、提交审核：
driver.find_element_by_class_name('btn btn-success product_pub').click()
#4、下架商品：
driver.find_element_by_class_name('btn btn-warning product_pub').click()


# #页面跳转：
# #以文本定位进行页面跳转：上一页、下一页、首页、尾页、
# driver.find_element_by_link_text("要执行的操作").click()
# #点击页面进行跳转：下方示例为跳转到第一页
# driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div/div[4]/div[1]/div[7]/ul/li[3]/a').click()

#分配代理商：
#代理商搜索框：
driver.find_element_by_class_name('form-control').click()
#开始搜索输入的代理商：
driver.find_element_by_class_name('form-control btn btn-primary').click()

#确认分配代理商：
driver.find_element_by_id('assign-btn').click()

#添加商品页面：
#标题输入框：
driver.find_element_by_class_name('form-control').click()

#系列选择下拉框：
driver.find_element_by_class_name('form-control').click()




#获得当前URL并打印

url = driver.current_url

print (url)


title = driver.title

print (driver.title)

if title == u"错误情况":

    print ("title 名称正确!")

else:

    print ("title 名称错误!")

driver.current_url
time.sleep(3)


driver.close()



