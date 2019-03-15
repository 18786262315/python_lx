import re,copy,requests,os
from urllib.parse import quote


# 起点数据
urls = "http://api.singmap.com/broke-manager-service/siteplan/updateSiteContent"

yuanshishujiu = [{"width":"72","height":"25","left":"411","top":"89","name":"Rect0","fill":"rgba(220,20,60,0.4)","type":"rect","buildingID":"dc1cb41f25da45d795e38fee3113e8e5","sitePlanID":"ff140c8bb89d4f5dbb22031f485be1fb","unitID":"c0725a8df14b47e48abf0124b8250241","sitePlanName":"Block 2"},{"width":"72","height":"25","left":"1502","top":"85","name":"Rect1","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"72","height":"25","left":"408","top":"736","name":"Rect2","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"72","height":"25","left":"1504","top":"734","name":"Rect3","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"72","height":"24","left":"403","top":"1375","name":"Rect4","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"72","height":"24","left":"1057","top":"1377","name":"Rect5","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"72","height":"24","left":"1699","top":"1379","name":"Rect6","fill":"rgba(220,20,60,0.4)","type":"rect"}]
jieguo = [] #执行完成的结果存放
hang = [23,23,23,23,22,23,21] #行
lie = [9,8,9,8,6,6,9] #列
unit_name = 0 #名称

for name in yuanshishujiu:
    #循环原始列表
    #获取需要改变的数据
    height = int(copy.deepcopy(name.get('height')))
    width = int(copy.deepcopy(name.get('width')))
    top = int(copy.deepcopy(name.get('top')))
    left = int(copy.deepcopy(name.get('left')))
    # 获取当前执行的块需要循环多少行列。
    dy_hang = hang.pop(0)
    dy_lie = lie.pop(0)
    for i in range(dy_hang):
        #一级循环
        #循环完成一行后，需要重置一次列
        lefts = left
        # 当前行位置加上块高度
        for a in range(dy_lie):
            #二级循环
            name["top"] = "%s"%(top)
            name["left"] = "%s"%(lefts)
            name["name"] = "Rect%s"%(unit_name)
            unit_name+=1
            jieguo.append(copy.deepcopy(name))
            print(name.items())
            # 循环一次增加一次列的距离，距离==块的宽度
            lefts+=width+(3 if a%3  else 2)
        top = '%s'%(int(name.get('top'))+height+(3 if i%3  else 2))


# 推送到服务器
jieguo = re.sub("'",'"','%s'%jieguo)
content = quote('%s'%jieguo,'utf-8') #转码
payload = {"userId": "6",
           "token": "54a408e0ffc048fb9f8591e038b4ae27",
           "brokeId": "0c5d80359cc5416a9ea953fdebcbfc20",
           "sitePlanId": "e1d6caf9ec7542f5aa20248cb3e913d5",
           "content": jieguo
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls,data=payload)
print(ret)


# 写入文件
jieguo_w = open(R'C:\Users\Administrator\Desktop\names01\jieguo.txt','r+',encoding='utf-8')
jieguo_w.write('%s'%jieguo)



