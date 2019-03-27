import re,requests


def pdt_wb(urls,content):
    # 推送到服务器
    content = re.sub("'", '"', '%s' % content)  # 将单引号换成双引号
    content = re.sub("\n", '', '%s' % content)  # 去除换行符
    # content = quote('%s' % content, 'utf-8')  # 转码
    payload = {"userId": "12",
            "token": "433bc525d0194606b2a030c446e1f526",
            "brokeId": "6b6c528605b445689fd8995cfe5f4f13",
            "sitePlanId": "671cdc6bdc464858915a5adc0b21e68c",
            "content": content
            }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    ret = requests.post(urls, data=payload)
    print(ret)