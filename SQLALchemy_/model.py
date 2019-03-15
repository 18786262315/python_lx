#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.util import aliased
# mysql+pymysql 链接方式://root:ycc962464 账户密码@127.0.0.1:3306链接地址及端口/tests链接的数据库名称?charset=utf8mb4 字符集
engine = create_engine(
    "mysql+pymysql://root:ycc962464@127.0.0.1:3306/tests?charset=utf8mb4", max_overflow=5,echo=True)

Base = declarative_base(engine)

# 创建单表


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)  # 主键 autoincrement=True 自增
    name = Column(String(32))
    extra = Column(String(16))
    num = Column(Integer)
    tests = Column(String(20))
    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra','tests'),  # 索引
        # Index('my_index', my_table.c.data, mysql_length=10) length 索引长度
        #Index('a_b_idx', my_table.c.a, my_table.c.b, mysql_length={'a': 4,'b': 9})
        # Index('my_index', my_table.c.data, mysql_prefix='FULLTEXT') 指定索引前缀
        # Index('my_index', my_table.c.data, mysql_using='hash') 指定索引类型
    )


class Home(Base):
    __tablename__ = 'home'
    id = Column(Integer, primary_key=True)
    tab = Column(String(20))
    values = Column(String(60))
    value_name = Column(String(40))


# 一对多


class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)  # unique 唯一


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))

# 多对多


class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))  # 外键
    group_id = Column(Integer, ForeignKey('group.id'))


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)

# 定义初始化数据库函数


def init_db():
    Base.metadata.create_all()

# 定义删除数据库函数

def drop_db():
    Base.metadata.drop_all()

# drop_db()
init_db()


Session = sessionmaker(bind=engine)  # 创建session
session = Session()


def search(name):
    user = Session.query.filter(User.name == name).first()
    if user is None or User.name.strip == '':
        print('用户不存在')
    else:
        print(' 用户 %s' % user.name)


# 增
# obj = User(name="111guanyu", extra='hanjiang') #添加单条
# session.add(obj) #加入到队列

# session.add_all([ #添加多条
#     User(name="liubei", extra='leader'),
#     User(name="zhangfei", extra='xiaodi'),
# ])
# session.commit()  # 添加到sql

# 删
# session.query(User).filter(User.id > 2).delete()
# session.commit()

# 改
# # 更新user表中id大于2的name列为099
# session.query(User).filter(User.id > 2).update({"name" : "099"})
# # 更新user表中id大于2的name列，在原字符串后边增加099
# session.query(User).filter(User.id > 2).update({User.name: User.name + "099"}, synchronize_session=False)
# # 更新user表中id大于2的num列，使最终值在原来数值基础上加1
# session.query(User).filter(User.id > 2).update({"num": User.num + 1}, synchronize_session="evaluate") # 数字相加，必须设置synchronize_session="evaluate"
# session.commit()


# 查

# ret = session.query(User).all() # 查询所有
# sql = session.query(User) # 查询生成的sql
# print(sql)
# ret = session.query(User.name, User.extra).all() #查询User表的name和extra列的所有数据
# ret = session.query(User).filter_by(name='alex').all()  # 取全部name列为alex的数据
# ret = session.query(User).filter_by(name='alex').first() # 第一个匹配name列为alex的数据

# ret是一个对象列表。这个对象可以通过 “对象[索引].字段”来获取对应的值

ret = session.query(User).all() #查询列表所有数据
# print(ret[0].name) #结果为元组，可通过下标的形式
# for i in ret: #循环元组，
#     print(i.name)


# 其他操作

#　条件
# ret = session.query(User).filter_by(name='alex').all() #查询所有name = alex 内容
# ret = session.query(User).filter(User.id > 1, User.name == 'eric').all() # 且的关系

# ret = session.query(User).filter(User.id.between(1, 3), User.name == 'eric').all()
# print(ret[0].name)
# ret = session.query(User).filter(User.id.in_([1,3,4])).all()
# print(ret)
# ret = session.query(User).filter(~User.id.in_([1,3,4])).all() # ~表示非。就是not in的意思
# print(ret)
# ret = session.query(User).filter(User.id.in_(session.query(User.id).filter_by(name='eric'))).all() # 联表查询
# print(ret)
# from sqlalchemy import and_, or_   # 且和or的关系
# ret = session.query(User).filter(and_(User.id > 3, User.name == 'eric')).all() # 条件以and方式排列

# # print(ret)
# ret = session.query(User).filter(or_(User.id < 2, User.name == 'eric')).all() # 条件以or方式排列
# for i in ret:
#     print(i.id)
# ret = session.query(User).filter(
#     or_( #这部分表示括号中的条件都以or的形式匹配
#         User.id < 2, # 或者 or User.id < 2
#         and_(User.name == 'eric', User.id > 3),# 表示括号中这部分进行and匹配
#         User.extra != ""
#     )).all()


# 通配符
# ret = session.query(User).filter(User.name.like('e%')).all()
# print(list(ret))

# ret = session.query(User).filter(~User.name.like('e%')).all() # 表示not like

# # 限制 limit用法
# ret = session.query(User)[0:3] # 等于limit ，具体功能需要自己测试 从几行到几行！
# ret = session.query(Favor).join(Person,Person.favor_id == Favor.nid).all()

# # 排序
# ret = session.query(User).order_by(User.name.desc()).all()
# ret = session.query(User).order_by(User.name.desc(), User.id.asc()).all() # 按照name从大到小排列，如果name相同，按照id从小到大排列

# # 分组
# from sqlalchemy.sql import func

# ret = session.query(User).group_by(User.extra).all()
# ret = session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id)).group_by(User.name).all()

# ret = session.query(
#     func.max(User.id),
#     func.sum(User.id),
#     func.min(User.id)).group_by(User.name).having(func.min(User.id) >2).all() # having对聚合的内容再次进行过滤
# print(ret)

# 连表

# ret = session.query(User, Favor).filter(User.id == Favor.nid).all()

# ret = session.query(Person).join(Favor).all()
# # 默认是inner join
# ret = session.query(Person).join(Favor, isouter=True).all() # isouter表示是left join
# print(ret)
# # 组合
# q1 = session.query(User.name).filter(User.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all() #union默认会去重
# print(ret)
# for i in ret:
#     print(i)
# q1 = session.query(User.name).filter(User.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all() # union_all不去重
# print(ret)
