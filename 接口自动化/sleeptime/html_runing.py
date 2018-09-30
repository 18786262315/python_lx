import unittest
from api_sleeptime import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('test_api_time.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='接口定时测试结果', 
                                description='执行结果统计：',
                                verbosity=2
                                )
        runner.run(suite)
