from app import app
import json
from flask import render_template
from flask_cors import *
CORS(app, resources=r'/*')
@app.route('/')
@app.route('/index',methods=["get"])

def falsk_2():

    res = ['zhangs','liss']
    return json.dumps(res,ensure_ascii="false")


@app.route('/indexs',methods=["get"])

def index():
    user = { 'nickname': 'Miguel' } # fake user
    return '''
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
    </body>
    </html>
    '''

@app.route('/logins',methods=['POST','get'])
def teste():
    nm ='cc'
    pd = '123456'
    #正常参数 请求
    # username = request.values.get('username')
    # print(username)
    # json格式参数 请求
    data = request.get_data()
    json_data = json.loads(data.decode("utf-8"))
    print(json_data['username'])
    
    if json_data['username'] == nm:
        if json_data['passowd'] == pd:
            res = {'mags':{'name':'cc','yar':'5220','values':'666'},'ucode':0}
            return json.dumps(res,ensure_ascii=False)
        else:
            res = {'mags':'密码错误！！','ucode':2}
            return json.dumps(res,ensure_ascii=False)
    else:
        res = {'mags':'账号错误！！','ucode':1}
        return json.dumps(res,ensure_ascii=False)


    res ={'msage':k,'ucode':0}
    return json.dumps('res',ensure_ascii=False)

