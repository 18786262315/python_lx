# --*-- coding:utf-8 --*--

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner
from time import sleep


class TestMixgo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('初始化测试内容')
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(600, 1078)
        self.driver.get('http://www.mixgo.com/app_v3')

    @classmethod
    def tearDownClass(self):
        print('结束本次测试！！')
        self.driver.quit()

    def test_tab(self):
        '''tab'''
        sleep(2)
        self.click('id', 'tab-t0-1')
        sleep(1)
        self.click('id', 'tab-t0-2')
        sleep(1)
        self.click('id', 'tab-t0-3')
        sleep(1)
        self.click('id', 'tab-t0-4')
        sleep(1)
        self.click('id', 'tab-t0-0')
        sleep(2)

    def test_so(self):
        '''搜索'''
        sleep(2)
        # self.click('id','auto')
        self.send('class', 'searchbar-input', '沙发')
        self.driver.find_element_by_class_name(
            'searchbar-input').send_keys(Keys.ENTER)
        self.click(
            'xpath', '//*[@id="mainTabs"]/page-product-search/ion-header/ion-navbar/button')
        sleep(2)

    def test_city(self):
        '''城市选择'''
        sleep(2)
        self.click(
            'xpath', '//*[@id="tabpanel-t0-0"]/page-tab-home/ion-header/ion-navbar/ion-buttons[1]/button')
        sleep(2)
        self.send(
            'xpath', '//*[@id="mainTabs"]/page-city-select/ion-header/ion-toolbar/div[2]/ion-searchbar/div/input', '上海')
        sleep(2)
        self.click(
            'xpath', '//*[@id="mainTabs"]/page-city-select/ion-content/div[2]/ion-list/ion-item-group/ion-item')
        sleep(2)
        s = self.text(
            'xpath', '//*[@id = "tabpanel-t0-0"]/page-tab-home/ion-header/ion-navbar/ion-buttons[1]/button/span/span')

        self.assertEqual('上海市', s)
        sleep(1)
    # def test_main_banber(self):
    #    #滚动条定位失败
    #   self.click('xpath','//*[@id="tabpanel-t0-0"]/page-tab-home/ion-content/div[2]/ion-slides/div/div[1]/ion-slide[4]/div')
    #   self.data()
    #   self.back()

    def test_fenlei(self):
        '''类目查看'''
        sleep(1)
        self.driver.find_element_by_xpath(
            "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/ion-grid/ion-row/ion-col[1]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='mainTabs']/page-unit-list/ion-header/ion-navbar/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/ion-grid/ion-row/ion-col[2]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='mainTabs']/page-product-list/ion-header/ion-navbar/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/ion-grid/ion-row/ion-col[3]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='mainTabs']/page-product-list/ion-header/ion-navbar/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/ion-grid/ion-row/ion-col[4]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='mainTabs']/page-product-list/ion-header/ion-navbar/button").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/ion-grid/ion-row/ion-col[5]").click()
        sleep(2)
        self.click('id', 'tab-t0-0')
        sleep(2)

    def test_mendian(self):
        '''查看门店以及门店详情'''
        s = 1
        sleep(2)
        self.click(
            'xpath', "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/div[1]/div[1]")
        for i in range(4):
            sleep(1)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-store-list/ion-content/div[2]/div/div["+str(s)+"]")
            sleep(2)
            self.click(
                'xpath', '//*[@id="mainTabs"]/page-store-detail/ion-header/ion-navbar/button')  # 返回
            s += 1
        sleep(2)
        self.click(
            'xpath', '//*[@id="mainTabs"]/page-store-list/ion-header/ion-navbar/button')
        sleep(2)

    def test_xinxuan(self):
        '''今日新选'''
        s = 1
        sleep(2)
        self.click(
            'xpath', "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/div[2]/div[1]")
        sleep(1)
        for i in range(10):
            sleep(1)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-today-news/ion-content/div[2]/div/div["+str(s)+"]/div")
            sleep(2)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-product-detail/ion-header/ion-navbar/button")
            s += 1
        sleep(1)
        self.click(
            'xpath', "//*[@id='mainTabs']/page-today-news/ion-header/ion-navbar/button")
        sleep(1)

    def test_quanjing(self):
        '''全景搭配'''
        sleep(2)
        self.click(
            'xpath', "//*[@id='tabpanel-t0-0']/page-tab-home/ion-content/div[2]/div[3]/div")
        sleep(1)
        s = 1
        for i in range(3):
            sleep(1)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-pano-list/ion-content/div[2]/ion-card["+str(s)+"]")
            sleep(2)
            p = 1
            for i in range(3):
                self.click(
                    'xpath', "//*[@id='mainTabs']/page-pano-detail/ion-content/div[2]/div[2]/div["+str(p)+"]/div")
                sleep(2)
                self.click(
                    'xpath', "//*[@id='mainTabs']/page-product-detail/ion-header/ion-navbar/button")
                sleep(1)
                p += 1

            self.click(
                'xpath', "//*[@id='mainTabs']/page-pano-detail/ion-header/ion-navbar/button")
            s += 1
        sleep(2)

        self.click(
            'xpath', '//*[@id="mainTabs"]/page-pano-list/ion-header/ion-navbar/button')

        sleep(2)

    def test_temai(self):
        '''特卖好物'''
        sleep(2)
        s = 1
        self.click(
            'xpath', "//*[@id = 'tabpanel-t0-0']/page-tab-home/ion-content/div[2]/div[4]/div[1]/div")
        sleep(1)
        for i in range(10):
            sleep(1)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-best-goods/ion-content/div[2]/div/div["+str(s)+"]/div")
            sleep(2)
            self.click(
                'xpath', "//*[@id='mainTabs']/page-product-detail/ion-header/ion-navbar/button")
            s += 1
        sleep(1)
        self.click(
            'xpath', "//*[@id='mainTabs']/page-best-goods/ion-header/ion-navbar/button")

    def click(self, name, key):
        if name == 'id':
            self.driver.find_element_by_id(key).click()
        if name == 'class':
            self.driver.find_element_by_class_name(key).click()
        if name == 'xpath':
            self.driver.find_element_by_xpath(key).click()

    def send(self, name, key, value):
        if name == 'id':
            self.driver.find_element_by_id(key).send_keys(value)
        if name == 'class':
            self.driver.find_element_by_class_name(key).send_keys(value)
        if name == 'xpath':
            self.driver.find_element_by_xpath(key).send_keys(value)

    def text(self, name, key):
        if name == 'id':
            self.driver.find_element_by_id(key).text
        if name == 'class':
            self.driver.find_element_by_class_name(key).text
        if name == 'xpath':
            self.driver.find_element_by_xpath(key).text

    def back(self, name):
        if name == 1:
            self.driver.find_element_by_xpath(
                "//*[@id='mainTabs']/page-product-list/ion-header/ion-navbar/button").click()
        if name == 2:
            self.driver.find_element_by_xpath(
                "//*[@id='mainTabs']/page-unit-list/ion-header/ion-navbar/button").click()

    def data(self):
        title = self.driver.title
        self.driver.get_screenshot_as_file("D:\\ycc\\test\\"+title+".png")


if __name__ == '__main__':
    unittest.main(verbosity=2)
