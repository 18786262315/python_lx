

import requests
import lx_yanzhengma as yzm


sign = 'c96eb4b9022c6b155181c18cb2017319'


header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko'}

# 不带上Cookie就访问不了这个页面
cookie = "hiido_ui=0.5414506156088357; hd_newui=0.93335198871822; JSESSIONID=837e1ee535325d5c7afaf8e9e3a301597c9e14cf; hdjs_session_id=0.2418187863152595; hdjs_session_time=1559646455527"

# 将上面哪个cookie转化成字典类型
cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}

print(cookie_dict)

get_codes = 'https://zc.yy.com/reg/pc/chk.do'
get_post = 'https://api.51yudiao.com/api/app/user/register'

mobile = yzm.get_phone()


print(mobile)

s = requests.Session()


def fs(mobile):
    requests.packages.urllib3.disable_warnings()
    get_code = s.post(get_codes, headers=header_dict, cookies=cookie_dict, verify=False, data={
        'passport': '13846667842', 'mobilefix': '', 'appid': '5037'})
    return get_code


fa = fs(mobile)
print(fa.request.headers)
print(fa.headers)
print(fa.text)

while fa.text :
    yzm.time.sleep(2)
    print(fa.text)
    fa = fs(mobile)


code = yzm.get_code(mobile)
print(code)


pull_phone = s.post(get_post, headers=header_dict, data={
    'phone': mobile, 'captcha': code, 'password': 'ycc962464'})

print(pull_phone.status_code)
