
import requests
import os
from urllib.parse import quote


def getManyPages(keyword,pages):
    params=[]
    for i in range(30,30*pages+30,30):
        params.append({
                      'tn': 'resultjson_com',
                      'ipn': 'rj',
                      'ct': 201326592,
                      'is': '',
                      'fp': 'result',
                      'queryWord': keyword,
                      'cl': 2,
                      'lm': -1,
                      'ie': 'utf-8',
                      'oe': 'utf-8',
                      'adpicid': '',
                      'st': -1,
                      'z': '',
                      'ic': 0,
                      'word': keyword,
                      's': '',
                      'se': '',
                      'tab': '',
                      'width': '',
                      'height': '',
                      'face': 0,
                      'istype': 2,
                      'qc': '',
                      'nc': 1,
                      'fr': '',
                      'pn': i,
                      'rn': 30,
                      'gsm': '1e',
                      '1488942260214': ''
                  })
    url = 'https://image.baidu.com/search/index'
    urls = []
    imgs =[]
    for i in params:
        urls.append(requests.get(url,params=i).json().get('data'))
    
    # print(urls)
    for data in urls:
        for titles in  data:
            # print(titles.get('replaceUrl'))
            if titles.get('replaceUrl') != None:
                for uu in titles.get('replaceUrl'):
                    # print(uu.get("ObjURL"))
                    imgs.append(uu.get("ObjURL"))
            else:
                pass

    return imgs



def getImg(dataList, localPath):


    if not os.path.exists(localPath):  # 新建文件夹
        os.mkdir(localPath)

    x = 0
    for lists in dataList:
        try:
            if lists != None:
                print('正在下载：%s' % lists)
                code = requests.get(lists,timeout=5).status_code
                if code == 200:
                    ir = requests.get(lists)
                    open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
                else:
                    print('图片地址不存在')
            else:
                print('图片链接不存在')
        except Exception as e:
            continue

if __name__ == '__main__':
    dataList = getManyPages("男女",20)  # 参数1:关键字，参数2:要下载的页数
    getImg(dataList,"E:\\ycc\\pythonlianxi\\images\\") # 参数2:指定保存的路径