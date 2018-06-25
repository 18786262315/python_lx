import unittest
from test_b import AndroidTest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AndroidTest))

    with open('HTMLReport.html', 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='喜马拉雅FM', 
                                description='测试结果',
                                verbosity=2
                                )
        runner.run(suite)
