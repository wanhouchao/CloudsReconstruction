import pymysql
from Auto_testing_comm_platform.Config.TestEnv import *


class Mysqldb:
    def __init__(self, Mysqlserver, Mysqluser, Mysqlpwd, Mysqldatabase):
        self.Mysqlserver = Mysqlserver
        self.Mysqluser = Mysqluser
        self.Mysqlpwd = Mysqlpwd
        self.Mysqldatabase = Mysqldatabase

    def Execute(self, sql):
        # 远程连接上mysql的test
        self.conn = pymysql.connect(self.Mysqlserver, self.Mysqluser, self.Mysqlpwd, self.Mysqldatabase)
        print('连接成功')
        # 创建游标
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()  # 提取游标内容
            cursor.execute('commit')
            cursor.close()
            print("执行sql语句成功")
            return data
        except BaseException as e:
            print("执行sql语句失败")
            print(e)


if __name__ == '__main__':
    # sql = 'CREATE TABLE user_info (id INT(20) PRIMARY KEY,NAME CHAR(20),age INT(20),sex CHAR(20),salary INT(20),PASSWORD CHAR(20))'
    # sql = 'insert into user_info(id,name,age,sex,salary,password) values (1000,"万厚超",23,"男",213465321,123456)'
    # sql = 'DESC user_info'
    sql = "SELECT epsfrontserver.device_rfid_article_record.office_name,epsfrontserver.device_rfid_article_record.article_name ,epsfrontserver.device_rfid_article_record.position_name ,epsfrontserver.device_rfid_article_record.robot_name ,epsfrontserver.device_rfid_article_record.create_date FROM epsfrontserver.device_rfid_article_record WHERE epsfrontserver.device_rfid_article_record.create_date LIKE '2019-09-06%' ORDER BY epsfrontserver.device_rfid_article_record.create_date DESC;"
    db = Mysqldb(epsfrontserverServer, epsfrontserverUser, epsfrontserverPwd, epsfrontserverDatabase)
    data = db.Execute(sql)
    print(data)
