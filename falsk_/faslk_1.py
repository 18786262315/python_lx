# coding = utf8
import flask,json
import pymysql

"""post 传参加MySQL处理"""


server=flask.Flask(__name__)#__name__代表当前的python文件。把当前的python文件当做一个服务启动

@server.route('/index',methods=['post'])#第一个参数就是路径,第二个参数支持的请求方式，不写的话默认是get


def index():
    username=flask.request.values.get('username')
    passwd=flask.request.values.get('passwd')
    db = pymysql.connect(host='192.168.254.130', user='root',password='ycc962464', db='pp_list')
    cursor = db.cursor()
    sql = "select * from user where name='%s';"%(username)
    cursor.execute(sql)  # 执行sql语句
    shujuku_name = cursor.fetchall()
    
    if not shujuku_name:
        res = {'msg':'当前用户不存在','msg_code':0}
        sql = "INSERT INTO user(name,passowd) VALUES ('%s','%s')"%(username,passwd)
        cursor.execute(sql)  # 执行sql语句
        db.commit() # 同步数据，如果没有这个函数那么程序对数据库的操作，数据不会同步到数据库中，比如没有此函数，程序将数据插入数据库没有报错，但在数据库终端查询时，会发现数据表没有发生改变。再或者每次执行插入语句时，没有调用此函数，那么一旦程序运行过程中报错，之前插入成功的数据也不会保存到数据库中。所以建议每次对表进行修改，插入或删除操作后都调用一次此函数
    else:
        res ={'mag':'登录成功','mag_code':1}
    db.close()
    return json.dumps(res,ensure_ascii=False)

server.run(port=7777,debug=True,host='0.0.0.0')