# -*- coding:utf-8 -*-
import json
import pymysql


# print("id","code","name")
# 遍历结果
# print(results)


js = 'region_dumps.json'
noe = open('test_a.txt', 'a', encoding="utf-8")
with open(js, encoding="utf-8") as f:
    diqu = json.load(f)
    db = pymysql.connect(host='localhost', user='root',
                         password='', db='test_db')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    sql = "SELECT a.`code`,a.`name`,b.`name` from mr_district a,mr_city b where a.citycode=b.code"

    cursor.execute(sql)  # 执行sql语句

    shujuku_name = cursor.fetchall()
    for sheng in diqu:
        # print(sheng['name'])
        for shi in sheng['cities']:
            qu_ss = shi['counties']
            shi_name = shi['name']
            for qu in qu_ss:

                # print('区、县：',qu['name'])
                qu_name = qu['name']
                for row in shujuku_name:
                    # shi_name=shi_name
                    # print(shi_name)
                    # print('区、县：',qu['name'])
                    district_code = int(row[0])
                    district_name = row[1]
                    city_name = row[2]
                    # print(district_code,district_name,city_name)
                    code = district_code*100
                    if qu_name == district_name and shi_name == city_name:
                        for shanghui in qu['circles']:
                            district_code = district_code
                            code += 1
                            # noe.write(str(code)+'\t'+qu['name']+'\n')
                            shanghui_name = shanghui['name']
                            sql = "INSERT INTO mr_circles (code,name,districtcode) VALUES ("+"'"+str(
                                code)+"','"+str(shanghui_name)+"','"+str(district_code)+"');"
                            print(sql)
                            noe.write(sql+'\n')
                            cursor.execute(sql)

db.close()




sql = "INSERT INTO mr_circles (code,name,districtcode) VALUES ("+"'"+str(code)+"','"+str(shanghui_name)+"','"+str(district_code)+"');"
print(sql)

noe.write(sql+'\n')
cursor.execute(sql)


