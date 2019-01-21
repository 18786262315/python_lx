from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time

htmlunit = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
htmlunit.get("http://www.cnblogs.com/shuaiqing/p/7742382.html")
print (htmlunit.title)

# htmlunit.find_element_by_id('kw').send_keys(u'杨彦星')
# print (htmlunit.find_element_by_id('kw').get_attribute('type'))
# print (htmlunit.find_element_by_id('kw').size) #打印输入框的大小
# htmlunit.find_element_by_id('su').click()
html = htmlunit.execute_script("return document.documentElement.outerHTML")
print(html)
time.sleep(3)
html2 = htmlunit.find_element_by_xpath("//*").get_attribute("outerHTML")
print (html2)
# print(htmlunit.page_source)
# time.sleep(5)
# source=htmlunit.find_element_by_xpath("/html/body/script[6]").getAttribute("innerHTML")
# print(source)
