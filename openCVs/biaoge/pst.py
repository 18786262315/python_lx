import re,requests


def pdt_wb(urls,content):
    # 推送到服务器
    content = re.sub("'", '"', '%s' % content)  # 将单引号换成双引号
    content = re.sub("\n", '', '%s' % content)  # 去除换行符
    # content = quote('%s' % content, 'utf-8')  # 转码
    payload = {"userId": "6",
            "token": "7adb772a8bf1480bac74670082bd366a",
            "brokeId": "0c5d80359cc5416a9ea953fdebcbfc20",
            "sitePlanId": "dfee14ecac154b5f9e09dec7468399cb",
            "content": content
            }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    ret = requests.post(urls, data=payload)
    

    print(ret.text)