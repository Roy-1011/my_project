import mysql.connector

connection = mysql.connector.connect(host = 'localhost', 
                                     port = '3306',
                                     user = 'root',
                                     password = 'oyangwei7365o',
                                     database = 'db')

cursor = connection.cursor()

# 新增
# cursor.execute('INSERT INTO `account` VALUES("12345@gmail.com", "54321wasd");')

# 修改
# cursor.execute('UPDATE `db` SET `password` = ??? WHERE `email` = ???;')

# 刪除
# cursor.execute("DELETE FROM `db` WHERE `email` = ???;")

cursor.close()
connection.commit() # 只要是會改變資料的指令都要加這行
connection.close()