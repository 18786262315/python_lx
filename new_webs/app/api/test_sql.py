from app import app,db,json
from app.models import Role,User

@app.route('/test')
def test():
    db.session.add(Role(names='Adminss'))
    db.session.add(Role(names='Moderatorss'))
    db.session.add(Role(names='Userss'))
    db.session.commit()
    return json.dumps({'code':'0',"msg":"source"},ensure_ascii=False)









# db.session.add_all([User(username='john',role_id=1),User(username='susan',role_id=3),User(username='david',role_id=3)])
# db.session.commit()