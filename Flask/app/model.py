#!usr/bin/python
# -*- coding : utf-8 -*-

from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例
# from app.db import Model,Column,text,or_,and_,Column,Boolean,Date,Time,INT,Text,DateTime,DECIMAL,Float,Enum,Integer,String,ForeignKey,UniqueConstraint,Index,create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    passowd = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return self.name,self.phone

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    passowd = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return self.name


# class User(Model):
#     __tablename__ = "user"
#     id = Column(Integer,primary_key=True)
#     username = Column(String(20))
#     userpassword = Column(String(40))
#     phone = Column(String(20))
#     poto = Column(String(20)) #用户头像
#     createtime = Column(DateTime)
#     sex = Column(Enum('1','2','3','4'))


# class Person(Model):
#     __tablename__ = "person"
#     id = Column(Integer , primary_key=True , autoincrement=True)
#     age = Column(Integer)
#     name = Column(String(20))
#     price1 = Column(Float)
#     price2 = Column(DECIMAL(7,3))
#     delete = Column(Boolean)
#     sex = Column(Enum("男","女"))
#     create_time1 = Column(Date)
#     create_time2 = Column(DateTime)
#     create_time3 = Column(Time)
#     content = Column(Text)
#     contents = Column(LONGTEXT)
