from appium import webdriver
from time import sleep
import unittest
import test_a
import test_w

class AndroidTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = test_a.a_url()
        sleep(5)

    @classmethod
    def tearDownClass(self):
        self.driver.close_app()

    def test_tab(self):
        '''tab'''
        print(self.driver.contexts)# 获取上下文列表
        cons = self.driver.contexts  #保存上下文
        self.driver.switch_to.context('WebView in com.tencent.tim')
        # self.driver.page_source
        print(self.driver.current_context)
        print(self.driver.page_source)

    #     sleep(2)
    #     self.swipLeft()
    #     sleep(2)
    #     self.swipLeft()
    #     sleep(2)
    #     self.driver.tap([(345,1158)])
    #     sleep(2)

    #     sleep(2)
    #     self.click('id', 'tab-t0-1')
    #     sleep(1)
    #     self.click('id', 'tab-t0-2')
    #     sleep(1)
    #     self.click('id', 'tab-t0-3')
    #     sleep(1)
    #     self.click('id', 'tab-t0-4')
    #     sleep(1)
    #     self.click('id', 'tab-t0-0')
    #     sleep(2)

    # def test_bark1(self):
    #     self.click_id('cancel_btn')
    #     self.click_id('tab_liste')
    #     self.click_id('tab_finding')
    #     self.click_id('tab_myspace')
    #     self.click_id('main_play_icon_img')
    #     self.click_id('tab_home_page')
    #     sleep(3)

    # def test_bark2(self):
    #     self.click_list('分类')
    #     self.click_list('热门')
    #     self.click_list('精品')
    #     self.click_list('直播')
    #     self.click_list('广播')
    #     sleep(3)

    # def test_bark3(self):
    #     sleep(3)

    # def test_bark4(self):
    #     sleep(3)
    # def test_bark5(self):
    #     sleep(3)

    # def click(self, name, key):
    #     if name == 'id':
    #         self.driver.find_element_by_id(key).click()
    #     if name == 'class':
    #         self.driver.find_element_by_class_name(key).click()
    #     if name == 'xpath':
    #         self.driver.find_element_by_xpath(key).click()
    # def getSize(self):
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     return (x, y)

    # def swipLeft(self):
    #     t=1000
    #     l = self.getSize()
    #     x1 = int(l[0]*0.75)
    #     y1 = int(l[1]*0.5)
    #     x2 = int(l[0]*0.05)
    #     self.driver.swipe(x1, y1, x2, y1, int(t))

if __name__ == "__main__":
    unittest.main(verbosity=2)
