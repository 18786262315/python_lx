from threading import Thread
import time
import logging
import os


def login(ll):
    # import logging
    # logger = logging.getLogger(__name__)
    # logger.setLevel(level = logging.INFO)
    # handler = logging.FileHandler(ll)
    # handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)

    # console = logging.StreamHandler()
    # console.setLevel(logging.INFO)

    # logger.addHandler(handler)
    # logger.addHandler(console)

    # logger.info("Start print log")
    # logger.debug("Do something")
    # logger.warning("Something maybe fail.")
    # logger.info("Finish")
    os.system('adb logcat -v time process > %s'%ll)
    print('*——————————————————————————————————————————————*')


def sayhi(name_):
    f = open(name_)

    while True:

        content = f.readline()

        if content == '':

            break

        content = content.srtip().split()
        print(content)

    f.close()
    # with open(name_, 'r',encoding='utf-8') as f:
    #     while True:
    #         t = f.readlines()
    #         for i in t:
    #             print(i)
    #     print('*——————————————————————————————————————————————*')
        # for i in t:
        #     print(i)
# sayhi('log.txt')

if __name__ == '__main__':
    t = []
    t1 = Thread(target=login, args=('E:\\ycc\\pythonlianxi\\lx\\log.txt', ))
    t.append(t1)
    t2 = Thread(target=sayhi, args=('E:\\ycc\\pythonlianxi\\lx\\log.txt',))
    t.append(t2)
    for i in t:
        i.setDaemon(True)
        i.start()
    time.sleep(2)
    print('主线程')