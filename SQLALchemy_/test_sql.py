
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text,or_,and_,Column,Boolean,Date,Time,INT,Text,DateTime,DECIMAL,Float,Enum,Integer,String,ForeignKey,UniqueConstraint,Index,create_engine
from sqlalchemy.orm import sessionmaker,relationship,aliased
from sqlalchemy.dialects.mysql import LONGTEXT
import panduan_ku


host = 'mysql'
phost = 'pymysql'
name = 'root'
passw = 'ycc962464'
url = '127.0.0.1:3306'
database_name = 'new_sql'
charset = 'utf8mb4'
INT_GO = "%s+%s://%s:%s@%s"%(host,phost,name,passw,url)

#查看库是否创建 
ku = panduan_ku.Ku_Name
ku.panduan_ku(INT_GO,database_name)

engine = create_engine("{INT_GO}/{database_name}?charset={charset}".format(INT_GO=INT_GO,database_name=database_name,charset=charset),max_overflow=5,) #echo=True 是否打印回显

Base = declarative_base(engine)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    username = Column(String(20))
    userpassword = Column(String(40))
    phone = Column(String(13))
    poto = Column(String(20)) #用户头像
    createtime = Column(DateTime)
    sex = Column(Enum('1','2','3','4'))


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer , primary_key=True , autoincrement=True)
    age = Column(Integer)
    name = Column(String(20))
    price1 = Column(Float)
    price2 = Column(DECIMAL(7,3))
    delete = Column(Boolean)
    sex = Column(Enum("男","女"))
    create_time1 = Column(Date)
    create_time2 = Column(DateTime)
    create_time3 = Column(Time)
    content = Column(Text)
    contents = Column(LONGTEXT)





Base.metadata.create_all()
