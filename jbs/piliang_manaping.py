import re,copy,requests,os
from urllib.parse import quote


# 起点数据
urls = "http://api.singmap.com/broke-manager-service/siteplan/updateSiteContent"

yuanshishujiu = [{"width":"24","height":"11","left":"48","top":"283","name":"Rect0","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"24","height":"11","left":"474","top":"471","name":"Rect3","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"24","height":"11","left":"474","top":"111","name":"Rect4","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"49","height":"23","left":"52","top":"235","name":"Rect492","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"48","height":"23","left":"474","top":"65","name":"Rect493","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"48","height":"23","left":"474","top":"425","name":"Rect494","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"47","height":"11","left":"53","top":"259","name":"Rect495","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"48","height":"11","left":"475","top":"88","name":"Rect496","fill":"rgba(220,20,60,0.4)","type":"rect"},{"width":"48","height":"11","left":"475","top":"448","name":"Rect497","fill":"rgba(220,20,60,0.4)","type":"rect"}]
jieguo = [] #执行完成的结果存放
hang = [13,14,14,1,1,1,2,2,2] #行数 top
lie = [12,12,12,6,6,6,6,6,6] #列数 left
unit_name = 0 #名称
def panduan (name):
    #矫正行距
    if name in [3,9,15,21,25]:
        # if name[%2]:
        #     return 0
        # else:
        #     return 1
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
            #二级循环
            name["top"] = "%s"%(top)
            name["left"] = "%s"%(lefts)
            name["name"] = "Rect%s"%(unit_name)
            unit_name+=1
            jieguo.append(copy.deepcopy(name))
            print(name.items())
            # 循环一次增加一次列的距离，距离==块的宽度
            lefts+=width+(0 if a%3  else 0)
        top = '%s'%(int(name.get('top'))+height+panduan(i))
# +(1 if a%5  else 0)

# 推送到服务器
jieguo = re.sub("'",'"','%s'%jieguo) #将单引号换成双引号
content = quote('%s'%jieguo,'utf-8') #转码
payload = {"userId": "6",
           "token": "b88cf4564e6d47d79dd147398a93d5c3",
           "brokeId": "0c5d80359cc5416a9ea953fdebcbfc20",
           "sitePlanId": "fe036c3690364c2090a5ce180479616b",
           "content": jieguo
}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
ret = requests.post(urls,data=payload)
print(ret)


# 写入文件
# jieguo_w = open(R'C:\Users\Administrator\Desktop\names01\jieguo.txt','r+',encoding='utf-8')
# jieguo_w.write('%s'%jieguo)



