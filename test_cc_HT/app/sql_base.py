
from app import Base, log, LONGTEXT, Column, text, \
    or_, and_, Column, Boolean, Date, Time, INT, Text, \
    DateTime, DECIMAL, Float, Enum, Integer, String, \
    ForeignKey, UniqueConstraint, Index, create_engine, \
    relationship

# from sqlalchemy import


class User(Base):
    log.info('----->>用户表')
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    User_ID = Column(String(20), comment='用户ID')
    User_Name = Column(String(20), comment='用户昵称')
    User_Introduce = Column(String(40), comment='用户简介')
    User_Identity = Column(Enum('0', '1', '2'),
                           comment='用户身份：0、普通用户，1、草鸡管理员，2、临时用户')
    User_Phone = Column(Integer, comment='电话号码')
    User_Email = Column(String(20), comment='邮箱')
    User_Password = Column(String(40), comment='密码')
    File_ID = Column(String(20), comment='用户头像保存位置')
    Creation_Time = Column(DateTime, comment='用户创建日期')
    Last_Modified = Column(DateTime, comment='用户最后登录时间')
    Token = Column(String(20), comment='token')
    User_Status = Column(Enum('0', '1', '2', '3', '4', '5', '6'),
                         comment='用户状态：0、正常状态，1、未分配公司，2、未分配项目，3、账户已过期，4、账户冻结，5、账户异常，6、待定。。')


class Company_list(Base):
    log.info('----->>公司表')
    __tablename__ = 'company_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Company_ID = Column(String(20))
    Company_Name = Column(String(20), comment='公司名称')
    Company_Introd = Column(LONGTEXT, comment='公司介绍')
    Creation_Time = Column(DateTime, comment='公司创建时间')
    User_ID = Column(String(20), comment='创建人ID')


class User_Company(Base):
    log.info('----->>用户与公司关联表')
    __tablename__ = 'user_company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    User_ID = Column(String(20), comment='用户ID')
    Company_ID = Column(String(20), comment='公司ID')
    Company_Power_ID = Column(Integer, comment='公司权限ID')
    # User_Identity = Column(Enum(0,1,2,3,4,5,6),comment='用户在当前公司的身份：0、普通用户，1、管理员，2、BOSS，3、临时用户')


class Company_Power(Base):
    log.info('----->>用户所在公司内的权限表')
    __tablename__ = 'company_power'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Company_Power_ID = Column(Integer, comment='权限ID')
    Power_ID = Column(String(20), comment='权限名称')
    Power_Status = Column(Enum('0', '1', '2'),
                          comment='权限状态：0、有权限，1、没有权限，2、半权限')


class Item_list(Base):
    log.info('---->> 项目表')
    __tablename__ = 'item_list'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Item_ID = Column(String(20))
    Company_ID = Column(String(40), comment='公司ID')
    Item_Name = Column(String(20), comment='项目名称')
    Item_Introduce = Column(LONGTEXT, comment='项目介绍')
    Item_Status = Column(INT, comment='项目状态：0、正常进行，1、未开始，2、已结束，3、暂停项目，4、')
    Creation_Time = Column(DateTime, comment='项目创建日期')
    Last_Modified = Column(DateTime, comment='最后更新时间')
    User_ID = Column(String(20), comment='创建人ID')


class User_Item(Base):
    log.info('---->> 用户关联的项目表')
    __tablename__ = 'user_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    User_ID = Column(String(20), comment='用户ID')
    Item_ID = Column(String(20), comment='项目ID')
    Item_Power_ID = Column(Integer, comment='权限ID')


class Item_Power(Base):
    log.info('---->> 账户在项目内的权限表')
    __tablename__ = 'item_power'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Item_Power_ID = Column(Integer, comment='权限ID')
    Power_ID = Column(String(20), comment='权限名称')
    Power_Status = Column(Enum('0', '1', '2'),
                          comment='权限状态：0、有权限，1、没有权限，2、半权限')


class Power(Base):
    log.info('----->权限表')
    __tablename__ = 'power'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Power_ID = Column(String(20), comment='权限ID')
    Power_Name = Column(String(20), comment='权限名称')
    Power_Status = Column(Enum('0', '1', '2'),
                          comment='权限位置：0、公司权限，1、项目组权限，2、待定。。')


class Case(Base):
    log.info('----->用例表')
    __tablename__ = 'case'
    Case_ID = Column(Integer, primary_key=True,
                     autoincrement=True, comment='用例编号')
    Case_Title = Column(String(40), comment='用例标题')
    Case_Describe = Column(Text, comment='描述')
    File_ID = Column(String(20), comment='文件表ID')
    Case_Status = Column(Enum('1', '2', '3', '4', '5'),
                         comment='用例等级：1，2，3，4，5')
    User_ID = Column(String(20), comment='创建人ID')
    Responsibility_ID = Column(String(20), comment='责任人ID')
    Partake_ID = Column(String(20), comment='参与人')
    Item_ID = Column(String(20), comment='项目ID')


class File(Base):
    log.info('----->文件管理表')
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True, autoincrement=True, comment='用例编号')
    File_ID = Column(String(20), comment='文件ID')
    File_Position = Column(Text, comment='文件位置')


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    hobby_id = Column(Integer, ForeignKey("hobby.id"))  # 建FK关系

    # 与生成表结构无关，仅用于查询方便
    hobby = relationship("Hobby", backref='pers')  # 反向关联的名字


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    # engine = create_engine(
    #     "mysql+pymysql://root:123@127.0.0.1:3306/userinfo?charset=utf8",
    #     max_overflow=0,  # 超过连接池大小外最多创建的连接
    #     pool_size=5,  # 连接池大小
    #     pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    #     pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    # )

    Base.metadata.create_all()


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    # engine = create_engine(
    #     "mysql+pymysql://root:123@127.0.0.1:3306/userinfo?charset=utf8",
    #     max_overflow=0,  # 超过连接池大小外最多创建的连接
    #     pool_size=5,  # 连接池大小
    #     pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    #     pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    # )

    Base.metadata.drop_all(engine)


# if __name__ == '__main__':
    # drop_db()
init_db()
