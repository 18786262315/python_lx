
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR,text,or_,and_,Column,Boolean,Date,Time,INT,Text,DateTime,DECIMAL,Float,Enum,Integer,String,ForeignKey,UniqueConstraint,Index,create_engine
from sqlalchemy.orm import sessionmaker,relationship,aliased
from sqlalchemy.dialects.mysql import LONGTEXT
from Common.Log import Logger
from Config import ReadConfig
from app.sqls import kus
Logger = Logger(logger_name='Sql_access')
log = Logger.get_logger()
readc = ReadConfig()

INT_GO = "%s+%s://%s:%s@%s"%(readc.get_db('host'),readc.get_db('phost'),readc.get_db('username'),readc.get_db('password'),readc.get_db('url'))
kus.Ku_Name.Ku_(INT_GO,readc.get_db('database'))
engine = create_engine("{INT_GO}/{database_name}?charset={charset}".format(INT_GO=INT_GO,database_name=readc.get_db('database'),charset=readc.get_db('charset')),max_overflow=5,echo=False) #echo=True 是否打印回显

Base = declarative_base(engine)

class User(Base):
    log.info('----->>检测用户表')
    __tablename__ = "user"
    id = Column(Integer,primary_key=True , autoincrement=True)
    User_ID = Column(String(20),comment= '用户ID')
    User_Name = Column(CHAR,comment='用户昵称')
    User_Introduce = Column(String(40),comment='用户简介')
    User_Identity = Column(Enum(0,1,2),comment='用户身份：0、普通用户，1、草鸡管理员，2、临时用户')
    User_Phone = Column(Integer,comment='电话号码')
    User_Email = Column(CHAR,comment='邮箱')
    User_Password = Column(String(40),comment='密码')
    User_Photo = Column(CHAR,comment='用户头像保存位置')
    User_Status = Column(Enum(0,1,2,3,4,5,6),comment='用户状态：0、正常状态，1、未分配公司，2、未分配项目，3、账户已过期，4、账户冻结，5、账户异常，6、待定。。')


class Company_list(Base):
    log.info('----->>检测公司列表')
    __tablename__ = 'company_list'
    id = Column(Integer,primary_key=True , autoincrement=True)
    Company_ID = Column(String(20))
    Company_Name = Column(String(20),comment='公司名称')
    Company_Introd = Column(LONGTEXT,comment='公司介绍')
    Creation_Time = Column(DateTime,comment='公司创建时间')
    User_ID =Column(CHAR,comment='创建人ID')


class User_Company(Base):
    log.info('----->>检测用户与公司关联表')
    __tablename__='user_company'
    id = Column(Integer,primary_key=True , autoincrement=True)
    User_ID = Column(String(20),comment='用户ID')
    Company_ID = Column(String(20),comment='公司ID')
    User_Identity = Column(Enum(0,1,2,3,4,5,6),comment='用户在当前公司的身份：0、普通用户，1、管理员，2、BOSS，3、临时用户')


class Item_list(Base):
    log.info('---->> 检测项目表')
    __tablename__ = 'item_list'
    id = Column(Integer,primary_key=True , autoincrement=True)
    Item_ID = Column(String(20))
    Company_ID = Column(String(40),comment='公司ID')
    Item_Name = Column(CHAR,comment='项目名称')
    Item_Introduce = Column(LONGTEXT,comment='项目介绍')
    Item_Status = Column(INT,comment='项目状态：0、正常进行，1、未开始，2、已结束，3、暂停项目，4、')
    Creation_Time = Column(DateTime,comment='项目创建日期')
    Last_Modified = Column(DateTime,comment='最后更新时间')
    User_ID =Column(CHAR,comment='创建人ID')
    










Base.metadata.create_all()
