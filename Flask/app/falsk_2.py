
import flask,json
#!usr/bin/python
# -*- coding : UTF-8 -*-
import sys
import os
from flask_cors import *
from app import app
from flask import request,make_response,Response ,render_template, url_for
from app import db
from .model import users

CORS(app, resources=r'/*')
@app.route('/falsk_1',methods=["get"])
def falsk_1():
    print(request.args)
    res = {
    'ucode':0,
    'mags':{

    'list1':{'name':'cc','yar':'5220','values':'666','imgs':r"F:\BaiduNetdiskDownload\385.jpg"},
    'list2':{'name':'cc','yar':'5220','values':'777','imgs':r"F:\BaiduNetdiskDownload\383.jpg"},
    'list3':{'name':'cc','yar':'5220','values':'888','imgs':r"F:\BaiduNetdiskDownload\422.jpg"}
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

    # print(usersa[1:])
    return json.dumps({'data':username,'pass':password},ensure_ascii=False)

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
    # print(request.headers)
    # print(request.json)
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data['username'])
    print(json_data['password'])
    res ={'msage':{'username':json_data['username'],'password':json_data['password']},'ucode':0}
    return json.dumps(res,ensure_ascii=False)



@app.route('/test/<name>',methods=['get'])
def test(name):
    print(
'\n----->',request.method,
'\n----->',request.args,
'\n----->',request.form,
'\n----->',request.values,


'\n----->',request.cookies,


'\n----->',request.headers,




'\n----->',request.path,
'\n----->',request.full_path,

'\n----->',request.script_root,#?

'\n----->',request.url,
'\n----->',request.base_url,
    
'\n----->',request.url_root,
'\n----->',request.host_url,
'\n----->',request.host,
'\n----->',request.files,

)
    print(name)
    
    return json.dumps(name,ensure_ascii=False)

@app.route('/<int:age>/')  #设置url传参数 http://127.0.0.1:5000/18/
def first_flask(age):  #视图必须有对应接收参数
    print(age)
    return json.dumps('res',ensure_ascii=False)

@app.route('/a/<path:url>/')  #设置url传参数 http://127.0.0.1:5000/18/
def first(url):  #视图必须有对应接收参数
    print(url)
    return "hello word!!"

@app.route('/<path:url>',endpoint='name1')
def first_1(url):
    print(url_for('name1',url="/flask_1")) #如果设置了url参数，url_for（别名,加参数）
    return 'Hello World111'

def first_flask():
    return 'Hello World1111' 

app.add_url_rule(rule='/index/',endpoint='name2',view_func=first_flask,methods=['GET'])
#app.add_url_rule(rule=访问的url,endpoint=路由别名,view_func=视图名称,methods=[允许访问的方法])


# app.run(port=7777,debug=True,host='0.0.0.0')


