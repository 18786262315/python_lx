import requests



with open('baidu_tieba.png', 'ab') as f:
    r = requests.get('http://img.singmap.com/upload/broke/0c5d80359cc5416a9ea953fdebcbfc20/3d6835636d994508a27523d702a3e532/siteplanImg/8f5853da041240029196f6ef0dba2b55.jpg')
    f.write(r.content)
    f.close()




