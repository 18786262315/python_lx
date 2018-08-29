#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import time
import threading
import requests

lock = threading.RLock()
def run_api(url,n):
    
    lock.acquire()
    lock.acquire()
    lock.acquire()

    for i in range(n):
        end_ = requests.get(url)
        print(url)
        print(time.asctime)
    lock.release()
    lock.release()
    lock.release()

if __name__ == '__main__':


    t1 = threading.Thread(target=run_api,args=('http://www.baidu.com',30))
    t2 = threading.Thread(target=run_api,args=('http://www.cnblogs.com/yc-c/',20))
    t3 = threading.Thread(target=run_api,args=('http://www.voidcn.com/column/python/list-9.html',10))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

