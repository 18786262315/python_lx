import requests
import time

url = 'https://www.toutiao.com/api/pc/feed/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',

}

data = {
'category':'news_tech',
'utm_source':'toutiao',
'widen':2,
'max_behot_time':int(time.time()),
'max_behot_time_tmp':int(time.time()),
'tadrequire':'true',
'as':'A1C53D0BBF8999C',
'cp':'5DBF582FB82BAE1',
'_signature':'SY80XAAAFDGu-MxabuSUUEmPNE'}

# print(int(time.time()))


New_data = requests.get(url,headers=headers, data=data)
print(New_data.text)