#coding = utf8
import flask,json
import os
# import pathlib

server = flask.Flask(__name__)
@server.route('/falsk_1',methods=["get"])



def falsk_2():

    work_dir = 'E:\\ycc\\pythonlianxi'
    tt = os.listdir(work_dir)
    res = {'lists':tt}
    return json.dumps(res,ensure_ascii=False)
    
@server.route('/falsk_2',methods=['post'])

def tester():
    nm ='cc'
    pd = '123456'
    username = flask.request.values.get('username')
    passowd = flask.request.values.get('pass')
    if username == nm:
        if passowd == pd:
            res = {'mags':'hallo，word！！','ucode':0}
            return json.dumps(res,ensure_ascii=False)
        else:
            res = {'mags':'密码错误！！','ucode':2}
            return json.dumps(res,ensure_ascii=False)
    else:
        res = {'mags':'账号错误！！','ucode':1}
        return json.dumps(res,ensure_ascii=False)


    res ={'msage':k,'ucode':0}
    return json.dumps(res,ensure_ascii=False)



server.run(port=7777,debug=True,host='0.0.0.0')



