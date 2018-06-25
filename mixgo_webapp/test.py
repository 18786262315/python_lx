# --*-- coding:utf-8 --*--

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from HTMLTestRunner import HTMLTestRunner
# from time import sleep


# driver = webdriver.Chrome()
# driver.set_window_size(600, 1078)
# driver.get('http://www.mixgo.com/app_v3')


# # def click(name, key):
# #     if name == 'id':
# #         driver.find_element_by_id(key).click()
# #     if name == 'class':
# #         driver.find_element_by_class_name(key).click()
# #     if name == 'xpath':
# #         driver.find_element_by_xpath(key).click()


# sleep(2)
# driver.get_screenshot_as_file("D:\\apk\\shot1.png") # 截取当前屏幕。


# la = 'lal '.encode('utf-8')
# print(la)

foos = [1.0, 2.0, 3.0, 4.0, 5.0]
bars = [100, 200, 300, 400, 500]

def func(foo):
  index=foos.index(foo)
  print(foo)
print(list(map(func, foos)))
# def func(foo):
#   index = foos.index(foo) # foo在foos中的索引，拿她取出来
#   print(foo)
#   print(index) 
#   print(foo, bars[:][0:index] + bars[:][index+1:])
#   # 该索引同样在bars中相同位置，在切片的时候拿它取出，并拼接这个切片
#   # 大功告成！

# print(list(map(func, foos)))
# # print(func)