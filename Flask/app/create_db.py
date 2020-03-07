#!usr/bin/python
# -*- coding : utf-8 -*-
#创建表
from app import db
# from sqlalchemy import create_engine

db.create_all()




# host = 'mysql'
# phost = 'pymysql'
# name = 'root'
# passw = 'ycc962464'
# url = '127.0.0.1:3306'
# database_name = 'testt'
# charset = 'utf8mb4'

# 创建库
# urls = "%s+%s://%s:%s@%s"%(host,phost,name,passw,url)
# engine = create_engine(urls)
# conn = engine.connect()
# conn.execute("create database %s"%database_name)
# conn.close()