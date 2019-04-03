from app import session
from .sql_base import User,Company_list,File

session.add_all([
    User(
    User_ID = '1112',
    User_Name = 'cc',
    User_Introduce = 'hehea',
    User_Identity = '0',
    User_Phone = 1310000000,
    User_Email = '123@12.cc',
    User_Password = '123456',
    File_ID = 'file2',
    Creation_Time = '2019-02-23 23:00',
    Last_Modified = '2019-02-23 23:00',
    Token = 'casff234jh23ghj',
    User_Status = '0',
    ),
        User(
    User_ID = '1113',
    User_Name = 'cc1',
    User_Introduce = 'hehea1',
    User_Identity = '0',
    User_Phone = 1310000001,
    User_Email = '113@12.cc',
    User_Password = '123456',
    File_ID = 'file1',
    Creation_Time = '2019-02-23 23:00',
    Last_Modified = '2019-02-23 23:00',
    Token = 'casff234jh23ghj1',
    User_Status = '0',
    )
])
session.add_all([
    Company_list(    
    Company_ID = '1',
    Company_Name = '公司1',
    Company_Introd = 'Colssssssssssssss',
    Creation_Time = '2019-12-25 06:33',
    User_ID ='1112',
),
    Company_list(    
    Company_ID = '2',
    Company_Name = '公司3',
    Company_Introd = 'Colssssssssssssss',
    Creation_Time = '2019-12-25 06:33',
    User_ID ='1112',
),
    Company_list(    
    Company_ID = '3',
    Company_Name = '公司2',
    Company_Introd = 'Colssssssssssssss',
    Creation_Time = '2019-12-25 06:33',
    User_ID ='1113',
),
])


session.add_all([
    File(
    File_ID = 'file2',
    File_Position = R'test\ss\tss\ii.jpg'
    ),
    File(
    File_ID = 'file1',
    File_Position = R'test\ss\tss\ii2.jpg'
    ),
])

session.commit()
ret=session.query(User).all() #直接打印整个列表数据，以列表的形式返回

for i in ret:
    print(i.User_ID)



