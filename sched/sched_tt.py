
# import time
# import sched
 
# schedule = sched.scheduler ( time.time, time.sleep )
 
# def func(string1,float1):
#     print ("now is",time.time()," | output=",string1,float1)
 
# print (time.time())
# schedule.enter(10,0,func,("test1",time.time()))

# schedule.run()
# print (time.time())



import time
from threading import Timer
 
def print_time( enter_time ):
    print ("now is", time.time() , "enter_the_box_time is", enter_time)
 
 
print (time.time())
Timer(5,  print_time, ( time.time(), )).start()
Timer(10, print_time, ( time.time(), )).start()
print (time.time())