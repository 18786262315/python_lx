from app import app,db,json
from app.models import Users
@app.route('/')
@app.route('/index')
def index():
    users = Users.query.filter(Users.id > 3)
    lists =[]
    for i in users:
        alls ={}
        alls["names"] = i.name
        alls["ages"] = i.age
        lists.append(alls)
        print(i)
        print(i.name,i.age)
    return json.dumps({'msge':lists},ensure_ascii=False)
