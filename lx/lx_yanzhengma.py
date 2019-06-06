import requests
# import json
import re
import time

url = "http://api.fxhyd.cn/UserInterface.aspx"  # 网址
MOBILE = ""  # 电话号码
username = '843092012'  # 用户名
password = 'ycc962464'  # 密码
token = ''
itemid = '13780'  # 项目ID
header_dict = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
}


class yzm ():


def rq_get(date):
    Result = requests.get(url, headers=header_dict, params=date).text
    a = re.compile(r'\|', re.S)
    return a.split(Result)


def get_token():
    # 获取token
    token = rq_get(date={
        'action': 'login',
        'username': username,
        'password': password
    })[1]
    return token

token = get_token()

def get_user():
    # 获取用户信息
    balance = rq_get(date={'action': 'getaccountinfo', 'token': token})
    return balance


def get_phone():
    # 获取手机号码
    MOBILE = rq_get(
        date={
            'action': 'getmobile',
            'token': token,
            'itemid': itemid,
            'excludeno': '170.171.180.166',
            'timestamp': time.time()
        })

    if MOBILE[0] == 'success':
        MOBILE = MOBILE[1]
        return MOBILE
    else:
        return EOFError(MOBILE)
        print('获取TOKEN错误,错误代码' + MOBILE)


def get_code(MOBILE):
    # 获取短信，注意线程挂起5秒钟，每次取短信最少间隔5秒
    WAIT = 100  # 接收短信最长等待时间100s
    TIME1 = time.time()
    TIME2 = time.time()
    ROUND = 1
    
    text = rq_get(
        date={
            'action': 'getsms',
            'token': token,
            'itemid': itemid,
            'mobile': MOBILE,
            'release': '1',
            'timestamp': time.time()
        })
    while (TIME2 - TIME1) < WAIT and not text[0] == "success":
        time.sleep(5)  # 每过5秒获取一次验证码
        print(text)
        text = rq_get(
            date={
                'action': 'getsms',
                'token': get_token(),
                'itemid': itemid,
                'mobile': MOBILE,
                # 'release': '1',  # 是否立即释放号码 1、立即释放 ，如果不需要立即释放请不要带入该参数 。
                'timestamp': time.time()
            })
        TIME2 = time.time()
        ROUND = ROUND + 1

    # else:
    #     return EOFError('获取验证码超时！')

    if text[0] == "success":
        text = text[1]
        pat = "[0-9]+"
        IC = 0
        IC = re.search(pat, text)
        if IC:
            return IC
            # print("验证码是:\n" + IC.group())
        else:
            return '验证码提取失败，请检查正则匹配！'

    else:
        return '获取短信超时，错误代码是' + text[0] + ',循环数是' + str(ROUND)


# 释放号码
def Release_phone(MOBILE):
    release = rq_get(date={
        'action': 'release',
        'token': token,
        'itemid': itemid,
        'mobile': MOBILE
    })

    if release == 'success':
        return 'success'
        # print('号码成功释放')
