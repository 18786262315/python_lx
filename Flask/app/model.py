#!usr/bin/python
# -*- coding : utf-8 -*-

from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例

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