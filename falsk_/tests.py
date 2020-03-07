from flask import Flask,Blueprint,request
from flask_restful import Resource, Api,reqparse


app = Flask(__name__)
user_bp = Blueprint('user', __name__)
api = Api(app)
parser = reqparse.RequestParser()

# args = parser.parse_args()
def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)
    return wrapper


class DemoResource(Resource):
    method_decorators = [decorator1, decorator2]

    def get(self,test):


        print(test)
        return {'msg': 'get view'}

    def post(self):
        name = parser.add_argument('username', type=str)
        pasd = parser.add_argument('password', type=str)
        args = parser.parse_args()
        print(args)
        if name == 'admin' :
            return {
            'code': 0,
            'msg': '登录成功',
            'data': {
                'username':'admin',
                'password':'admin',
                'uuid': 'admin-uuid', 
                'name': '管理员',
                'token': '8dfhassad0asdjwoeiruty'
            }
            }
        else:
            return {'code':0, 'mag':'error'}


class DemoResources(Resource):
    method_decorators = {
          'get': [decorator1, decorator2],
          'post': [decorator1]
      }

    def get(self,tests):
        tests 
        return {'msg': 'get view',
                'ccc':tests}

    def post(self):
        return {'msg': 'post view1'}

api.add_resource(DemoResource, '/users/profile')
api.add_resource(DemoResources, '/users/profiled')

app.register_blueprint(user_bp)



# 此处启动对于1.0之后的Flask可有可无
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
