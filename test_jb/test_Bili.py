# -*- coding: utf-8 -*-
import unittest
from simulateBili import biliVideo
from HTMLTestRunner import HTMLTestRunner
import time

class testBili(unittest.TestCase):
    '''哔哩哔哩播放测试'''
    @classmethod
    def setUpClass(cls):
        testBili.bili=biliVideo()
        print('开始测试')

    @classmethod
    def tearDownClass(cls):
        print('结束测试')
        testBili.bili.driver.quit()

    def setUp(self):
        print('开始单个测试')

    def test_playPause(self):
        '''播放video和暂停测试'''
        self.bili.playPause()
        print(self.bili.driver.title)
        time.sleep(5)

    def tearDown(self):
        print('结束单个测试')
if __name__ == '__main__':
    unittest.main()