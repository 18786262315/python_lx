#! usr/bin/python3.6
# -*- coding : utf-8 -*-



# import pymysql  #导入 pymysql  


# # 打开数据库
# db = pymysql.connect('localhost','root','','test_db')

# #使用cursor()方法获取操作游标
# cursor = db.cursor()
# #sql
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('wwww', 'Mohan', 20, 'M', 201)"""
# try :
#     #执行sql
#     cursor.execute(sql)
#     db.commit()
# except:
#     #如果发生错误则回滚
#     db.rollback()

# #关闭数据库
# db.close()


# # 6 创建表
# # # 打开数据库连接
# db = pymysql.connect("localhost","root","","test_db" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
 
# cursor.execute(sql)
 
# # 关闭数据库连接
# db.close()




# # 5 打开数据库连接
# db = pymysql.connect("localhost","root","","test_db" )
 
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
 
# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT VERSION()")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()





# #4.删除操作  
# db= pymysql.connect(host="localhost",user="root",  
#     password="",db="test_db",port=3306)  
  
# # 使用cursor()方法获取操作游标  
# cur = db.cursor()  
  
# sql_delete ="delete from user where id = %d"  
  
# try:  
#     cur.execute(sql_delete % (4))  #像sql语句传递参数  
#     #提交  
#     db.commit()  
# except Exception as e:  
#     #错误回滚  
#     db.rollback()   
# finally:  
#     db.close()




# #3.更新操作  
# db= pymysql.connect(host="localhost",user="root",  
#     password="",db="test_db",port=3306)  
  
# # 使用cursor()方法获取操作游标  
# cur = db.cursor()  
  
# sql_update ="update user set name = '%s' where id = %d"  
  
# try:  
#     cur.execute(sql_update % ("xiongda",5))  #像sql语句传递参数  
#     #提交  
#     db.commit()  
# except Exception as e:  
#     #错误回滚  
#     db.rollback()   
# finally:  
#     db.close()  



# #2.插入操作  
# db= pymysql.connect(host="localhost",user="root",  
#     password="",db="test_db",port=3306)  
  
# # 使用cursor()方法获取操作游标  
# cur = db.cursor()  
  
# sql_insert ="""insert into user(id,name,age,work) values(5,'li','123','bushu')"""  
  
# try:  
#     cur.execute(sql_insert)  
#     #提交  
#     db.commit()  
# except Exception as e:  
#     #错误回滚  
#     db.rollback()   
# finally:  
#     db.close()  

  
# #打开数据库连接  
# db= pymysql.connect(host="localhost",user="root",  
#     password="",db="test_db",port=3306)  
  
# # 使用cursor()方法获取操作游标  
# cur = db.cursor()  
  
# #1.查询操作  
# # 编写sql 查询语句  user 对应我的表名  
# sql = "select * from user"  
# try:  
#     cur.execute(sql)    #执行sql语句  
  
#     results = cur.fetchall()    #获取查询的所有记录  
#     print("id","name","age")  
#     #遍历结果  
#     for row in results :  
#         id = row[0]  
#         name = row[1]  
#         password = row[2]  
#         print(id,name,password)  
# except Exception as e:  
#     raise e  
# finally:  
#     db.close()  #关闭连接








# 曲线图：
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()