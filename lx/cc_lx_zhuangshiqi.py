
# 装饰器： 修饰其他函数





  
import time


def test2(func):
	def test1():
		times_start= time.time()
		func()
		time_stop= time.time()
		print ('this is bar the run time: %s'% (time_stop-times_start))
	return test1

@test2
def bar():
	time.sleep(3)
	print('this is bar')

# bar=test2(bar)
bar()
# bar()