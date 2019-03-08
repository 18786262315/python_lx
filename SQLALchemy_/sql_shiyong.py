from test_sql import *


Session = sessionmaker(bind=engine)
session = Session()


#增加数据：

# obj = User(
    #单条
#     username='cc3',
#     userpassword='123456',
#     phone=18786262315,
#     poto='/names/php.png',
#     createtime='2019-12-23 12:22:32',
#     sex='3'
# )
# session.add(obj)

# session.add_all([
    #多条
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
# session.query(User).filter(User.id == 5).delete()

# 修改数据
# session.query(User).filter(User.id == 6).update({'username':'tset_cc'})

# session.query(User).filter(User.id == 7).update({User.username:'tset_ccc',User.phone:'13012345678'})

# session.commit()



ret=session.query(User).all()
ret = session.query(User.id, User.username).all()    #结果为一个列表
ret = session.query(User).filter_by(userpassword='123456').first()
# ret = session.query(User).filter_by(userpassword='123456').all()

# print(len(ret))
# for i in ret:
#     print(i.userpassword)
print(ret)
