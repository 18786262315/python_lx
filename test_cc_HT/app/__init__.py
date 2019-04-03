from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 配置文件读取
from Config import ReadConfig
readc = ReadConfig()

# 日志写入
from Common.Log import Logger
Logger = Logger(logger_name='Sql_access')
log = Logger.get_logger()

# 数据库链接
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker,relationship,aliased
from sqlalchemy.dialects.mysql import LONGTEXT
from app import kus
INT_GO = "%s+%s://%s:%s@%s"%(readc.get_db('host'),readc.get_db('phost'),readc.get_db('username'),readc.get_db('password'),readc.get_db('url'))
kus.Ku_Name.Ku_(INT_GO,readc.get_db('database')) #检测数据库是否存在，不存在则创建。
engine = create_engine("{INT_GO}/{database_name}?charset={charset}".format(INT_GO=INT_GO,database_name=readc.get_db('database'),charset=readc.get_db('charset')),max_overflow=5,echo=False) #echo=True 是否打印回显
Base = declarative_base(engine)

Session = sessionmaker(bind=engine)
session = Session()


from app import sql_base,sqls





