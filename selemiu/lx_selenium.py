
# #text文本定位
# driver.find_element_by_link_text("新闻").click()


# #iframe 子页面切换，操作
# driver.switch_to.frame(reference)# 进入
# driver.switch_to.parent_frame()#返回上一层
# driver.switch_to.default_content()#返回最顶层


#下拉框处理：
# from selenium.webdriver.support.select import Select
# #点击MixGo艺术品：
# Select(driver.find_element_by_id('filter-brand')).select_by_visible_text('MixGo艺术品')


# # 我的教程：http://www.cnblogs.com/TTyb/p/6046082.html
# from selenium import webdriver
# # 打开谷歌浏览器
# browser = webdriver.Chrome()
 
# # 打开窗口
# browser.get("https://www.baidu.com/")
# # 打开新窗口
# newwindow = 'window.open("https://www.baidu.com");'
# browser.execute_script(newwindow)
 
# # 切换到新的窗口
# handles = browser.window_handles
# browser.switch_to_window(handles[-1])












'''
新建实例
driver = webdriver.Chrome()

1.获取当前页面Url的函数
方法：current_url
实例：driver.current_url

2.表单的提交
方法：submit
解释:查找到表单（from）直接调用submit即可
实例：driver.find_element_by_id("form1").submit()

3.获取CSS的属性值
方法：value_of_css_property(css_name)
实例：driver.find_element_by_css_selector("input.btn").value_of_css_property("input.btn")

4.获取元素的属性值（一组元素中非常实用）
方法：get_attribute(element_name)
实例：driver.find_element_by_id("sellaiyuan").get_attribute("sellaiyuan")

5.判断元素是否被选中
方法：is_selected()
实例：driver.find_element_by_id("form1").is_selected()

6.返回元素的大小
方法：size
实例：driver.find_element_by_id("iptPassword").size
返回值：{'width': 250, 'height': 30}

7.判断元素是否显示（非常实用）
方法：is_displayed()
实例：driver.find_element_by_id("iptPassword").is_displayed()

8.判断元素是否被使用
方法：is_enabled()
实例：driver.find_element_by_id("iptPassword").is_enabled()

9.获取元素的文本值（非常实用）
方法：text
实例：driver.find_element_by_id("iptUsername").text

10.元素赋值
方法：send_keys(*values)
实例：driver.find_element_by_id("iptUsername").send_keys('admin')

11.删除浏览器所有的cookies
方法：delete_all_cookies()
实例：driver.delete_all_cookies()

12.删除指定的cookie
方法：delete_cookie(name)
实例：deriver.delete_cookie("my_cookie_name")

13.设置等待超时时间，可以在设置的时间内智能等待
方法：implicitly_wait(wait_time)
实例：driver.implicitly_wait(30)

14.查看浏览器的名字
方法：name
实例：drvier.name

15.打印title
方法：title
实例：driver.title

'''

#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver..keys import Keys #引入keys类操作
import time

def s(int):
    time.sleep(int)
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
print ('现在将浏览器最大化')
browser.maximize_window()
# text = browser.find_element_by_name('tj_duty').text
# print (text) #打印备案信息)

browser.find_element_by_id('kw').send_keys(u'杨彦星')
print (browser.find_element_by_id('kw').get_attribute('type'))
print (browser.find_element_by_id('kw').size) #打印输入框的大小
browser.find_element_by_id('su').click()
time.sleep(3)

print ('现在我将设置浏览器为宽480，高800显示')
browser.set_window_size(480,800)
browser.get('http://m.mail.10086.cn')
time.sleep(3)

print ('现在我将回到刚才的页面')
browser.maximize_window()
browser.back()
time.sleep(3)

print ('现在我将回到之前的页面')
browser.forward()
time.sleep(5)
print ('现在我将打开杨彦星的网站进行json搜索')
browser.get('http://www.yangyanxing.com')
browser.find_element_by_xpath("//*[@id='sidebar']/div[1]/form/input[1]").send_keys(u'json')
browser.find_element_by_xpath("//*[@id='sidebar']/div[1]/form/input[1]").send_keys(Keys.ENTER)

# browser.find_element_by_xpath(".//*[@id='header']/div[1]/div/form/input[2]").click()
time.sleep(5)
browser.quit()

browser = webdriver.Chrome()

print ('以下将以登录人人网来进行上面的综合应用')
browser.get('http://www.renren.com/SysHome.do')
browser.find_element_by_id('email').clear()#这个是以id选择元素
browser.find_element_by_id('email').send_keys('email')
browser.find_element_by_id('email').send_keys(Keys.BACK_SPACE)
time.sleep(2)
browser.find_element_by_id('email').send_keys('m')
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL,'a')
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL,'x')#剪切掉里面的内容
s(2)
browser.find_element_by_id('email').send_keys(Keys.CONTROL,'v') #重新输入进去
s(2)
browser.find_element_by_name('password').clear()#这个是以name选择元素
browser.find_element_by_name('password').send_keys('password')
#browser.find_element_by_xpath(".//*[@id='login']").click()#这个是以xpath选择元素
browser.find_element_by_xpath(".//*[@id='login']").send_keys(Keys.ENTER) #这里通过点击Enter键来登录
browser.maximize_window()
article = browser.find_element_by_link_text(u'周碧华：社科院出现内鬼意味着什么？')
ActionChains(browser).move_to_element(article).perform()#将鼠标移动到这里，但是这里不好用
ActionChains(browser).context_click(article).perform()
time.sleep(5)

browser.quit()





'''
Webdriver中比较常用的操作元素的方法：

clear()    清除输入框的默认内容

send_keys("xxx")    在一个输入框里输入xx内容

——如果输入中文，则需要在脚本开头声明编码为utf-8，然后在中文字符前面加u(如：send_keys(u"中文内容"))

click()    点击一个按钮

submit()    提交表单

 

WebElement接口常用方法：

size    返回元素的尺寸

——如：size = driver.find_element_by_id("id").size

text    获取元素的文本

——如：text = driver.find_element_by_id("id").text

get_attribute(name)    获得属性值

——如：attribute = driver.find_element_by_id("id").get_attribute(‘type‘)

is_displayed()    设置该元素是否用户可见

——如：isshow = driver.find_element_by_id("id").is_displayed()

 

ActionChains类鼠标操作的常用方法：

引入ActionChains类：from selenium.webdriver.common.action_chains import ActionChains

context_click()    右击

——如：RightClick = driver.find_element_by_id("id")

           ActionChains(driver).context_click(RightClick).perform()

double_click()    双击

——如：DoubleClick = driver.find_element_by_name("name")

           ActionChains(driver).double_click(DoubleClick).perform()

drag_and_drop(source, target)    鼠标拖放

——source：鼠标按下的源元素；target：鼠标释放的目标元素

——如：element = driver.find_element_by_name("name")

           target = driver.find_element_by_name("name")

           ActionChains(driver).drag_and_drop(element, target).perform()

move_to_element()    鼠标悬停在一个元素上

——如：above = driver.find_element_by_xpath("xpath路径")

           ActionChains(driver).move_to_element(above).perform()

click_and_hold()    按下鼠标左键在一个元素上

——如：left = driver.find_element_by_name("name")

           ActionChains(driver).click_and_hold(left).perform()

 

键盘事件：

引入Keys类包：from selenium.webdriver.common.keys import Keys

send_keys()    输入框输入内容

——如：driver.find_element_by_id("id").send_keys("XXX")

send_keys(Keys.BACK_SPACE)    向左删除一个字符                                             

——如：driver.find_element_by_id("id").send_keys("XXX")

send_keys(Keys.SPACE)    输入空格

——如：driver.find_element_by_id("id").send_keys(Keys.SPACE)

send_keys(Keys.CONTROL,‘a‘)    ctrl+a 全选输入框的内容

——如：driver.find_element_by_id("id").send_keys(Keys.CONTROL,‘a‘)

send_keys(Keys.CONTROL,‘x‘)    ctrl+x 剪切输入框的内容

——如：driver.find_element_by_id("id").send_keys(Keys.CONTROL,‘x‘)

send_keys(Keys.CONTROL,‘v‘)    ctrl+v 粘贴到输入框

——如：driver.find_element_by_id("id").send_keys(Keys.CONTROL,‘v‘)

send_keys(Keys.ENTER)    回车代替点击

——如：driver.find_element_by_id("id").send_keys(Keys.ENTER)

send_keys(Keys.TAB)    制表键(Tab)

——如：driver.find_element_by_id("id").send_keys(Keys.TAB)

send_keys(Keys.ESCAPE)    回退键（Esc）

——如：driver.find_element_by_id("id").send_keys(Keys.ESCAPE) 

send_keys(Keys.CONTROL,‘c‘)    复制

——如：driver.find_element_by_id("id").send_keys(Keys.CONTROL,‘c‘)  

 

打印信息

#获得title并打印

title = driver.title

print title

#拿当前title名称进行预期比较

if title == u"百度一下，你就知道":

　　print "title yes!"

else:

　　print "title no!"

#获得当前URL并打印

url = driver.current_url

print url

 

等待时间

#导入 WebDriverWait 包
from selenium.webdriver.support.ui import WebDriverWait
#导入 time 包
import time

sleep()    设置固定等待时间

——如：time.sleep(5)  #等待5秒

implicitly_wait()   #等待一个元素被发现，或一个命令完成，超出了设置时间则抛出异常

——如：driver.implicitly_wait(30)

           driver.find_element_by_id("id").click()

WebDriverWait()    在设置时间内，默认每隔一段时间检测检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常

WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)

——driver：WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)

——timeout：最长超时时间，默认以秒为单位

——poll_frequency：休眠时间的间隔（步长）时间，默认为 0.5 秒

——ignored_exceptions：超时后的异常信息，默认情况下抛 NoSuchElementException 异常

——如1：element = WebDriverWait(driver, 10).until(lambda x : x.find_element_by_id("id"))

           element.send_keys("selenium")

——如2：element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(“Id”))

            is_disappeared = WebDriverWait(driver, 30, 1, (ElementNotVisibleException)).until_not(lambda x: x.find_element_by_id(“someId”).is_displayed())

WebDriverWai()一般由 unit()或 until_not()方法配合使用:

——until(method, message=’’)
      调用该方法提供的驱动程序作为一个参数，直到返回值不为 False。
——until_not(method, message=’’)
      调用该方法提供的驱动程序作为一个参数，直到返回值为 False。

 

定位一组对象

#选择当前页面上所有tag name为input的元素

inputs = driver.find_elements_by_tag_name(‘input‘)

#从中过滤出type为checkbox的元素，并勾选上

for input in inputs:

　　if input.get_attribute(‘type‘) == ‘checkbox‘:

　　　　input.click()

#使用CSS定位选择所有type为checkbox的元素，并勾选上

checkboxes = driver.find_elements_by_css_selector(‘input[type=checkbox]‘)

for checkbox in checkboxes:

　　checkbox.click()

#把最后一个checkbox的勾去掉    pop()为空则是最后一个

driver.find_elements_by_css_selector(‘input[type=checkbox]‘).pop().click()
'''





