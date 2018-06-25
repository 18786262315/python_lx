


from appium import webdriver
from time import sleep

#以下为启动session时的desired capabilities的设置
desired_caps = {
    "platformName": "Android",
    "platformVersion": "4.4.2",
    "deviceName": "emulator-5554",
    "appPackage": "com.ximalaya.ting.android",
    "appActivity": "com.ximalaya.ting.android.host.activity.MainActivity",
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True

  }
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.1.1'
# desired_caps['deviceName'] = 'c76dc6fa'
# #desired_caps['app']='D:\software\Android\APPS\com.tencent.mm_621.apk'，这个是要安装的app的安装包地址，不是必须的，有#这个项的话会先通过这个地址安装app，我没有用这个，直接用的Package名和activity名
# desired_caps['appPackage'] = 'com.baidu.searchcraft'
# desired_caps['appActivity'] = 'com.baidu.searchcraft.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#driver.find_element_by_id("com.smartisanos.calculator:id/digit2").click()


driver.activate_ime_engine('输入法包名') #激活输入法：
driver.activate_ime_engine('com.android.inputmethod.latin/.LatinIME')
driver.find_element_by_accessibility_id(u"搜索").send_keys('1234')

driver.active_ime_engine #获取当前输入法的包名和Activity
i= driver.active_ime_engine
print(i)

driver.add_cookie({}) #添加cookie
driver.add_cookie({'name':'BAIDUID','value':'AAAAAAAAAAAAAA:FG=1'})

driver.app_strings #获取应用的字符串。
s = driver.app_strings
print(s)

driver.application_cache #创建一个应用缓存 ----用法暂时未知！
driver.available_ime_engines #获取当前设备可用的输入法：
a = driver.available_ime_engines
print(a)

driver.back() #返回，与driver.keyevent(4)，结果相同

driver.background_app('时间') #将APP放置在后台一段时间，时间到了之后再打开 
driver.background_app(10)

driver.close() # 关闭当前窗口

driver.close_app() # 关闭APP，在设备上停止正在运行的应用程序，在所需的功能中指定

# 在native和html5混合页面测试时，需要在native层和H5层切换，所以首先需要得到context层级的名称
driver.context #当前会话的当前上下文
driver.contexts #列出所有的可用上下文 
driver.current_context #列出当前上下文
driver.switch_to.context(None) #将上下文切换到默认上下文  

driver.create_web_element #创建带有指定elementid的web元素 ,在Selenium WebDriver中重写方法，以便始终给它们Appium WebElement

driver.command_executor #与远程WebDriver服务器的连接。详情：https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol

driver.current_activity #检索设备上运行的当前活动

driver.current_package#获取当前运行的包名

driver.current_url #获取当期页面的URL

driver.current_window_handle #返回当前窗口的句柄

driver.deactivate_ime_engine #关闭当前的输入法：
a = driver.active_ime_engine
print('当前输入法是：'+a)
driver.deactivate_ime_engine()

driver.delete_all_cookies #删除会话范围内的所有cookie

driver.delete_cookie("my_cookie") #删除指定的cookie

driver.desired_capabilities # 返回启动参数

driver.device_time #返回设备上的日期和时间

driver.drag_and_drop(el1,el2) #拖动元素
el1 = driver.find_element_by_id("host_banner_img")
el2 = driver.find_element_by_id("main_tiv_cover")
driver.drag_and_drop(el1[0],el2[0]) #将el1拖动到el2

driver.end_test_coverage #没明白，翻译说：结束了覆盖范围的收集，并将其覆盖。

driver.error_handler #处理由WebDriver服务器返回的错误

driver.execute #执行脚本

driver.execute_async_script #在当前窗口/帧中异步执行JavaScript。
script = "var callback = arguments[arguments.length - 1]; " \
          "window.setTimeout(function(){ callback('timeout') }, 3000);"
driver.execute_async_script(script)


driver.execute_script #在当前窗口/帧中同步执行JavaScript。
driver.execute_script('return document.title;')


driver.file_detector #检测本地磁盘上的文件。

driver.file_detector_context


#定位
driver.find_element

driver.find_element_by_accessibility_id

driver.find_element_by_android_uiautomator

driver.find_element_by_class_name

driver.find_element_by_css_selector

driver.find_element_by_id

driver.find_element_by_ios_class_chain

driver.find_element_by_ios_predicate

driver.find_element_by_ios_uiautomation

driver.find_element_by_link_text

driver.find_element_by_name

driver.find_element_by_partial_link_text

driver.find_element_by_tag_name

driver.find_element_by_xpath

driver.find_elements

driver.find_elements_by_accessibility_id

driver.find_elements_by_android_uiautomator

driver.find_elements_by_class_name

driver.find_elements_by_css_selector

driver.find_elements_by_id

driver.find_elements_by_ios_class_chain

driver.find_elements_by_ios_predicate

driver.find_elements_by_ios_uiautomation

driver.find_elements_by_link_text

driver.find_elements_by_name

driver.find_elements_by_partial_link_text

driver.find_elements_by_tag_name

driver.find_elements_by_xpath



driver.flick #滑动

driver.forward # 在浏览器历史上向前迈进了一步。

driver.fullscreen_window #全屏

driver.get #在当前浏览器打开一个网页

driver.get_cookie #对比cookie，相同返回cookie ，否则返回none
driver.get_cookie('my_cookie')

driver.get_cookies #返回一组字典，对应于当前会话中可见的Cookie。
driver.get_cookies()

driver.get_log #获取给定日志类型的日志。
driver.get_log('browser')
driver.get_log('driver')
driver.get_log('client')
driver.get_log('server')

driver.get_screenshot_as_base64 #将当前窗口的屏幕截图获取为Base64编码字符串。这在HTML中嵌入图像是有用的。
driver.get_screenshot_as_base64()

driver.get_screenshot_as_file #将当前窗口的屏幕截图保存到PNG映像文件。如果存在任何IOrror，则返回true。在文件名中使用完整路径。
driver.get_screenshot_as_file('/Screenshots/foo.png')

driver.get_screenshot_as_png #将当前窗口的屏幕截图，以二进制数据获取。
driver.get_screenshot_as_png()

driver.get_settings #返回当前会话的AppServer设置。不要将设置与期望的能力混淆，它们有不同的概念。参见HTTPS://GithuB.COM/APIUM/APIUM/BBU/MIST/DOCS/En/AdvestEng/StutsM.MD。

driver.get_window_position #获取当前窗口的x，y位置。
driver.get_window_position()

driver.get_window_rect #获取窗口的x、y坐标以及当前窗口的高度和宽度。
driver.get_window_rect()

driver.get_window_size #获取当前窗口的宽度和高度。
driver.get_window_size()

driver.hide_keyboard #在输入完内容后收起键盘，让‘输入法’遮挡的按钮可以被点击
driver.activate_ime_engine('com.baidu.input_miv6/.ImeService')
driver.find_element_by_id("输入框").click()
sleep(5)
driver.hide_keyboard()


'''设置粘性超时以隐式等待找到元素，或完成命令,如果超出时间则抛出异常。这种方法只需要每次调用一次。
当使用了隐式等待执行测试的时候，如果 WebDriver没有在DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常
一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。'''
driver.implicitly_wait #隐式等待，相比sleep 高级
driver.implicitly_wait('时间')

driver.install_app #安装app
driver.install_app('Apk路径')

driver.is_app_installed #检查app安装情况（返回true/false)
driver.is_app_installed('package_name')

driver.is_ime_active() #检测是否有输入法被启用，返回true/False
a = driver.is_ime_active()
print(a)

driver.keyevent #向设备发送物理按键代码。仅安卓系统。
driber.keyevent('键值')

driver.launch_app #启动APP，无需传值。

driver.lock # 锁定设备一段时间。仅iOS。 时间单位为秒。

driver.log_types #获取可用日志类型的列表。

driver.long_press_keycode #长按键

driver.maximize_window #浏览器窗口最大化

driver.minimize_window #浏览器窗口最小化

driver.mobile #没明白

driver.name #查看浏览器的名字

driver.network_connection #查看当前的网络连接状态 0、无 000 1、飞行模式 2、wifi 4、数据连接 6、wifi+数据连接

driver.open_notifications #打开通知栏

driver.orientation #设置设备屏幕的方向 

driver.page_source #获取当前页面的树形结构源代码，与uiautomatorviewer截屏所展示出来的结构是相同的
c = driver.page_source
print (c)

driver.pinch #缩放
pinch(self, element=None, percent='缩放百分比（可选参数）', steps='步骤数量（可选参数）') 
driver.pinch('缩放元素')


driver.press_keycode 

driver.pull_file

driver.pull_folder

driver.push_file

driver.quit

driver.refresh

driver.remove_app # 卸载app
driver.remove_app("package_name,APP包名")

driver.reset

driver.save_screenshot

driver.scroll

driver.session_id

driver.set_location

driver.set_network_connection

driver.set_page_load_timeout

driver.set_script_timeout

driver.set_value

driver.set_window_position

driver.set_window_rect

driver.set_window_size

driver.shake

driver.start_activity

driver.start_client

driver.start_session

driver.stop_client

driver.swipe

driver.switch_to.

driver.switch_to_active_element

driver.switch_to_alert

driver.switch_to_default_content

driver.switch_to_frame

driver.switch_to_window

driver.tap

driver.title

driver.toggle_location_services

driver.toggle_touch_id_enrollment

driver.touch_id

driver.update_settings

driver.w3c

driver.wait_activity

driver.window_handles

driver.zoom































