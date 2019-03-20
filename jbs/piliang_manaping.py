import re,copy,requests,os
from urllib.parse import quote


# 起点数据
urls = "http://192.168.0.145:9998/broke-manager-service/siteplan/updateSiteContent"

yuanshishujiu = [{"width":"54","height":"40","left":"150","top":"157","name":"Rect1265","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"59","height":"40","left":"206","top":"157","name":"Rect1266","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"267","top":"157","name":"Rect1267","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"66","height":"40","left":"328","top":"157","name":"Rect1268","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"395","top":"157","name":"Rect1269","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"61","height":"40","left":"456","top":"157","name":"Rect1270","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"518","top":"157","name":"Rect1271","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"67","height":"40","left":"580","top":"157","name":"Rect1272","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"55","height":"40","left":"648","top":"157","name":"Rect1273","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"55","height":"40","left":"706","top":"157","name":"Rect1274","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"762","top":"157","name":"Rect1275","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"68","height":"40","left":"976","top":"157","name":"Rect1276","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"54","height":"40","left":"1047","top":"157","name":"Rect1277","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"61","height":"40","left":"1102","top":"157","name":"Rect1278","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"54","height":"40","left":"1165","top":"157","name":"Rect1279","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"62","height":"40","left":"1221","top":"157","name":"Rect1280","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"1285","top":"157","name":"Rect1281","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"66","height":"40","left":"1346","top":"157","name":"Rect1282","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"1413","top":"157","name":"Rect1283","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"62","height":"40","left":"1474","top":"157","name":"Rect1284","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"61","height":"40","left":"1536","top":"157","name":"Rect1285","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"71","height":"40","left":"1598","top":"157","name":"Rect1286","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"1822","top":"157","name":"Rect1287","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"54","height":"40","left":"1885","top":"157","name":"Rect1288","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"1941","top":"157","name":"Rect1289","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"60","height":"40","left":"2002","top":"157","name":"Rect1290","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"67","height":"40","left":"2063","top":"157","name":"Rect1291","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"61","height":"40","left":"2130","top":"157","name":"Rect1292","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"62","height":"40","left":"2193","top":"157","name":"Rect1293","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"68","height":"40","left":"2258","top":"157","name":"Rect1294","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"69","height":"40","left":"2328","top":"157","name":"Rect1295","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"55","height":"40","left":"2399","top":"157","name":"Rect1296","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"55","height":"40","left":"2456","top":"157","name":"Rect1297","fill":"rgba(220,20,60,0.4)","type":"rect"}]
jieguo = [] #执行完成的结果存放
hang = [39 for i in range(22)]#行数 top
hang.extend(37 for i in range(11))
lie = [1 for i in range(22)]+[1 for i in range(11)] #列数 left
unit_name = 0 #名称
def panduan (name):
    #矫正行距
    if name %3:
        return 1
    else:
        return 1

for name in yuanshishujiu:
    #循环原始列表
    #获取需要改变的数据
    height = int(copy.deepcopy(name.get('height')))
    width = int(copy.deepcopy(name.get('width')))
    top = int(copy.deepcopy(name.get('top')))
    left = int(copy.deepcopy(name.get('left')))
    # 获取当前执行的块需要循环多少行列。
    dy_hang = hang.pop(0)
    print(dy_hang)
    dy_lie = lie.pop(0)
    for i in range(dy_hang):
        #一级循环
        #循环完成一行后，需要重置一次列
        lefts = left
        # 当前行位置加上块高度
        for a in range(dy_lie):
            name["width"] = "%s"%(width)
            name["left"] = "%s"%(lefts)
            #二级循环
            name["top"] = "%s"%(top)
            name["name"] = "Rect%s"%(unit_name)
            unit_name+=1
            jieguo.append(copy.deepcopy(name))
            print(name.items())
            # 循环一次增加一次列的距离，距离==块的宽度
            lefts+=width+(1 if a%3  else 0)
        top = '%s'%(int(name.get('top'))+height+panduan(i))
# +(1 if a%5  else 0)

# 推送到服务器
jieguo = re.sub("'",'"','%s'%jieguo) #将单引号换成双引号
content = quote('%s'%jieguo,'utf-8') #转码
payload = {"userId": "6",
           "token": "238c7d59afd24ea0968d8201f91c5988",
           "brokeId": "0c5d80359cc5416a9ea953fdebcbfc20",
           "sitePlanId": "bce02fb00828405fab40399e663567b2",
           "content": jieguo
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls,data=payload)
print(ret)


# 写入文件
# jieguo_w = open(R'C:\Users\Administrator\Desktop\names01\jieguo.txt','r+',encoding='utf-8')
# jieguo_w.write('%s'%jieguo)



