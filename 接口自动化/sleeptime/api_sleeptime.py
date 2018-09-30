

import sched ,time,requests,os

schedule = sched.scheduler(time.time, time.sleep)

n_http = 'http://www.mixgo.com/'
n_https = 'https://www.mixgo.com/'

def p_http():
    '''执行http请求测试'''
    times = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    try:
        fanhuizhi = requests.get(n_http).status_code
        print('http当前时间：%s>>>'%times,fanhuizhi)

    except Exception as e:
        print ('\31[1;35m 发现时间》》》'+times+'《《《\31[0m')
        print(e)
        with open('E:\\ycc\\pythonlianxi\\11.txt','a',encoding='utf-8') as f:
            f.write('》》》http《《《\n》》》错误时间:%s《《《\n错误信息：%s\n\n'%(times,e))


def p_https():
        '''执行https请求测试'''
    times = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
    try:
        fanhuizhi = requests.get(n_https).status_code
        print('https当前时间：%s>>>'%times,fanhuizhi)

    except Exception as e:
        print ('发现时间》》》'+times+'《《《')
        print(e)
        with open('E:\\ycc\\pythonlianxi\\11.txt','a',encoding='utf-8') as f:
            f.write('》》》https《《《\n》》》错误时间:%s《《《\n错误信息：%s\n\n'%(times,e))


def perform_command(cmd, inc):
    # 安排inc秒后再次运行自己，即周期运行
    #防止报错后停止运行
    schedule.enter(inc, 0, perform_command, (cmd, inc))

    p_http()
    p_https()

def timming_exe(cmd, inc=60):
    # enter用来安排某事件的发生时间，从现在起第n秒开始启动
    schedule.enter(inc, 0, perform_command, (cmd, inc))
    # 持续运行，直到计划时间队列变成空为止
    schedule.run()


if __name__ == "__main__":
    timming_exe('echo %time%',10) #等待时间--秒