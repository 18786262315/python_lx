from test_sql import *
from test_sql import User

Session = sessionmaker(bind=engine)
session = Session()

user_all = User.query.all()
print(user_all)
# session.add(User(username='cc',userpassword='123456',phone='12345678901',poto='a.jpg',createtime='2019-12-23 12:22:32',sex='4'))
# session.commit()

#增加数据：

# obj = User(
#     # 单条
#     username='cc3',
#     userpassword='123456',
#     phone=18786262315,
#     poto='/names/php.png',
#     createtime='2019-12-23 12:22:32',
#     sex='3'
# )
# session.add(obj)

# session.add_all([
#     # 多条
#     User(
#         username='cc5',
#         userpassword='123456',
#         phone=18786262315,
#         poto='/names/php.png',
#         createtime='2019-12-23 12:22:32',
#         sex='3'),
#     User(
#         username='cc6',
#         userpassword='123456',
#         phone=18786262315,
#         poto='/names/php.png',
#         createtime='2019-12-23 12:22:32',
#         sex='3'),
#     User(
#         username='cc7',
#         userpassword='123456',
#         phone=18786262315,
#         poto='/names/php.png',
#         createtime='2019-12-23 12:22:32',
#         sex='3')
#         ])
# session.commit()


#删除数据
session.query(User).filter(User.id == 6).delete()


# 修改数据
# session.query(User).filter(User.id == 6).update({'username':'tset_cc'})

session.query(User).filter(User.id == 5).update({User.username:'tset_ccc',User.phone:'13012345678'})





# 查询
ret=session.query(User,Person).filter(User.id == Person.id).filter(Person.id == 1).all() #直接打印整个列表数据，以对象的形式返回
# ret=session.query(Users).all() #直接打印整个列表数据，以列表的形式返回
# ret=session.query(User.id,User.phone,User.username) # 打印指定列数据以元组的方式返回

# ret=session.query(User).order_by(User.username,-User.id) # 排序,可以单个排序也可以多个排序，加’-‘是表示倒序

# session.query(User.username.label('names')) # 以对指定列做别名

# users = aliased(User,name='users') # 感觉像是对表名称进行重命名
# ret = session.query(User,User.users)

# ret = session.query(User).limit(10) #limit(n) 返回查询到的指定条数数据
# ret = session.query(User).all()[0:3] #切片操作可以直接使用python内置的切片操作


# 带条件查询filter


# ret = session.query(User).filter(User.id == 1).all() #等值判断
# ret = session.query(User).filter(User.username != 'cc').all()  #非值判断 

# ret = session.query(User).filter(User.username.like('%tset%')).all()  #模糊查询 like

# ret = session.query(User).filter(User.id.in_([1,2,3,4,5,8])).all()  #范围内查询 in
# ret = session.query(User).filter(User.username.in_(session.query(User.username).filter(User.id.in_([1,2,3,4,5,6,9])))).all()  #范围查询
# ret = session.query(User).filter(~User.id.in_([1,2,3,4,5,8])).all()  #范围外查询 not in,在列名前面加’~‘号

# ret = session.query(User).filter(User.poto == None).all()  #判空 is null
# ret = session.query(User).filter(User.poto != None).all()  #不为空 is not null

# ret = session.query(User).filter(User.username.like(r'cc%'),User.phone =='18786262315').all() #and 条件
# ret = session.query(User).filter(User.username.like(r'cc%')).filter(User.phone =='18786262315').all() #and 条件
# ret = session.query(User).filter(and_(User.username.like(r'cc%'),User.phone =='18786262315')).all() #and 条件

# ret = session.query(User).filter(or_(User.username.like('cc%'),User.phone == 18786262315)).all() # or 条件

# ret = session.query(User).from_statement(text("select * from User where username like 'cc%'")).all() # 直接执行sql 语句
# ret = session.query(User).from_statement(text("select * from User where id =:name and username =:names")).params(name = 3,names='cc7').one() # 直接执行sql 语句


# ret = session.query(User).all() #all() 以列表的形式返回查询结果
# session.query(User).filter(..).one()/one_or_none()/scalar() #one()/one_or_none()/scalar()返回单独的一个数据对象



# ret = session.query(User.id, User.username).all()    #结果为一个列表
# ret = session.query(User).filter_by(userpassword='123456').first()
# ret = session.query(User).filter_by(userpassword='123456').all()
# ret=session.query(User.id,User.phone,User.username.label('names')).all()



print(type(ret))
for i in ret:
    for a in i:
        print(type(a))
        for s in a:
            print(s)

# print(ret.id)
