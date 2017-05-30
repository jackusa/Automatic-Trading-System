 # -*- coding: utf-8 -*-

import MySQLdb
# D:\MySQL\bin> mysql -u root -p 
class mySQL():
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = '211246'
        self.db = 'amarket'
        self.cur = []

    def connect(self):
        cnx = MySQLdb.connect(
            host = self.host, 
            port = self.port,
            user = self.user,
            passwd = self.passwd,
            db = self.db)
        return cnx


    def cursor(self):
        cur = self.connect().cursor()
        return cur



    def sqli(self):
        return "insert into stock values(%s, %s)"


cnx = mySQL().connect()
cur = mySQL().cursor()

cur.execute("create table new(time varchar(20), price varchar(20))") 

cur.execute(mySQL().sqli(),('9:52', '13.76'))

cur.close()
cnx.commit()
cnx.close()

