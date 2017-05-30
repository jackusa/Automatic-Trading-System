 # -*- coding: utf-8 -*-

import MySQLdb
# D:\MySQL\bin> mysql -u root -p

class mySQL() :
    def __init(self):
        self.cnx = []
        self.cur = []

    def cnx(self):
        self.cnx = MySQLdb.connect(
            host = 'localhost', 
            port = 3306,
            user = 'root',
            passwd = '211246',
            db = 'amarket')
        return self.cnx

    def cur(self):
        self.cur  = self.cnx.cursor()
        return self.cur

    def createTable(self, code):
        createTable = """create table N%s(
            Name varchar(20), 
            Open varchar(20), 
            CloseYesterday varchar(20),
            Close varchar(20), 
            Highest varchar(20), 
            Lowest varchar(20), 
            FirstBuy varchar(20), 
            FirstSell varchar(20), 
            Volume varchar(20), 
            Amount varchar(20), 
            Buy1stVol varchar(20), 
            Buy1st varchar(20), 
            Buy2ndVol varchar(20), 
            Buy2nd varchar(20), 
            Buy3rdVol varchar(20), 
            Buy3rd varchar(20), 
            Buy4thVol varchar(20), 
            Buy4th varchar(20), 
            Buy5thVol varchar(20), 
            Buy5th varchar(20), 
            Sell1stVol varchar(20), 
            Sell1st varchar(20), 
            Sell2ndVol varchar(20), 
            Sell2nd varchar(20), 
            Sell3rdVol varchar(20), 
            Sell3rd varchar(20), 
            Sell4thVol varchar(20), 
            Sell4th varchar(20), 
            Sell5thVol varchar(20), 
            Sell5th varchar(20), 
            Date varchar(20), 
            Time varchar(20))"""
        self.cur.execute(createTable, code)

    def inertValue(self, code, dataList):
        sqli="""insert into N%s values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s)"""
        self.cur.execute(sqli,(code, dataList[0], dataList[1], dataList[2], dataList[3], 
            dataList[4], dataList[5], dataList[6], dataList[7], dataList[8], dataList[9],
            dataList[10], dataList[11], dataList[12], dataList[13], dataList[14], dataList[15],
            dataList[16], dataList[17], dataList[18], dataList[19], dataList[20], dataList[21],
            dataList[22], dataList[23], dataList[24], dataList[25], dataList[26], dataList[27],
            dataList[28], dataList[29], dataList[30], dataList[31]))


    def close(self):
        self.cur.close()
        self.cnx.commit()
        self.cnx.close()


dataList=['222', 'Open', 'CloseYesterday', 'Close', 'Highest', 
        'Lowest', 'Buy1st', 'Sell1st', 'Volume', 'Amount', 
        'Buy1stVol', 'Buy1st', 'Buy2ndVol', 'Buy2nd', 'Buy3rdVol', 
        'Buy3rd', 'Buy4thVol', 'Buy4th', 'Buy5thVol', 'Buy5th', 
        'Sell1stVol', 'Sell1st', 'Sell2ndVol', 'Sell2nd', 'Sell3rdVol', 
        'Sell3rd', 'Sell4thVol', 'Sell4th', 'Sell5thVol', 'Sell5th', 
        'Date', 'Time']

int code = 1
print (str(code))
# mysql = mySQL()
# mysql.cnx()
# cur = mysql.cur()
# mysql.createTable('002504')
# mysql.inertValue(002502, dataList)
# mysql.close()

# cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
# cur.execute("delete from student where age='9'")

# SQL 插入语句
# sql = """INSERT INTO stock(time varchar(20), price varchar(20))
#          VALUES ('Mac', 'Mohan');"""


# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    cnx.commit()
# except:
#    # Rollback in case there is any error
#    cnx.rollback()

# # 关闭数据库连接
# cnx.close()


# create table 002500(
#             Name varchar(20), 
#             Open varchar(20), 
#             CloseYesterday varchar(20),
#             Close varchar(20), 
#             Highest varchar(20), 
#             Lowest varchar(20), 
#             Buy1st varchar(20), 
#             Sell1st varchar(20), 
#             Volume varchar(20), 
#             Amount varchar(20), 
#             Buy1stVol varchar(20), 
#             Buy1st varchar(20), 
#             Buy2ndVol varchar(20), 
#             Buy2nd varchar(20), 
#             Buy3rdVol varchar(20), 
#             Buy3rd varchar(20), 
#             Buy4thVol varchar(20), 
#             Buy4th varchar(20), 
#             Buy5thVol varchar(20), 
#             Buy5th varchar(20), 
#             Sell1stVol varchar(20), 
#             Sell1st varchar(20), 
#             Sell2ndVol varchar(20), 
#             Sell2nd varchar(20), 
#             Sell3rdVol varchar(20), 
#             Sell3rd varchar(20), 
#             Sell4thVol varchar(20), 
#             Sell4th varchar(20), 
#             Sell5thVol varchar(20), 
#             Sell5th varchar(20), 
#             Date varchar(20), 
#             Time varchar(20))

