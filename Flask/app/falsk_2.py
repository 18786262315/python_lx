#coding = utf8
import flask,json
import os
from flask_cors import *
from app import app
from flask import request,make_response,Response ,render_template
from app import db
from .model import users


CORS(app, resources=r'/*')
@app.route('/falsk_1',methods=["get"])
def falsk_1():

    res = {
    'ucode':0,
    'mags':{

    'list1':{'name':'cc','yar':'5220','values':'666','imgs':"F:\\BaiduNetdiskDownload\\风景系\\385.jpg"},
    'list2':{'name':'cc','yar':'5220','values':'777','imgs':"F:\BaiduNetdiskDownload\风景系\383.jpg"},
    'list3':{'name':'cc','yar':'5220','values':'888','imgs':"F:\BaiduNetdiskDownload\风景系\422.jpg"}
    }}
    return json.dumps(res,ensure_ascii=False)



@app.route('/login',methods=['POST','get'])
def tester():

    # json格式参数 请求
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    username = json_data['username']
    password = json_data['password']

    print(username)
    # newobj = users(phone=username,  passowd=password)
    # db.session.add(newobj)
    # db.session.commit()
    usersa = users.query.all()

    print(usersa[1:])
    return json.dumps({'data':'ccc'},ensure_ascii=False)

    #     # 使用cursor()方法获取操作游标
    #     cursor = db.cursor()
    #     sql = "SELECT * from users where phone = '%s' and passowd = '%s'" %(username,password)
    #     cursor.execute(sql)  # 执行sql语句
    #     shujuku_name = cursor.fetchall()
    #     print(shujuku_name)

    #     if shujuku_name[0] != ''  :
    #         if json_data['password'] == 'pd':
    #             res = {'mags':{'name':'cc','yar':'5220','values':'666'},'ucode':0}
    #             return json.dumps(res,ensure_ascii=False)
    #         else:
    #             res = {'mags':'密码错误！！','ucode':2}
    #             return json.dumps(res,ensure_ascii=False)
    #     else:
    #         res = {'mags':'账号错误！！','ucode':1}
    #         return json.dumps(res,ensure_ascii=False)


    #     res ={'msage':k,'ucode':0}
    #     return json.dumps('res',ensure_ascii=False)

    #     db.close()
    # except Exception as ee:
    #     # abort(400)
    #     raise ee




@app.route('/ucode',methods=['post','get'])
def code():
    return 'ss'


@app.route('/register',methods=['post','get'])

def register():

    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data['username'])
    print(json_data['password'])
    res ={'msage':{'username':json_data['username'],'password':json_data['password']},'ucode':0}
    return json.dumps(res,ensure_ascii=False)




# app.run(port=7777,debug=True,host='0.0.0.0')


