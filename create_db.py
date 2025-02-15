import mysql.connector

connection = mysql.connector.connect(host = 'localhost', 
                                     port = '3306',
                                     user = 'root',
                                     password = 'oyangwei7365o')

cursor = connection.cursor()

# 創建資料庫
# cursor.execute("CREATE DATABASE `db`;")

# 取得所有資料庫名稱
# cursor.execute("SHOW DATABASES;")
# records = cursor.fetchall()
# for r in records:
#     print(r)

# 選擇資料庫
# cursor.execute('USE `db`;')

# 創建表格
# cursor.execute('CREATE TABLE `account`(`email` VARCHAR(50) PRIMARY KEY,`password` VARCHAR(30));')

# 把值填入屬性裡
# cursor.execute('INSERT INTO `account` (email, password) VALUES("12345@gmail.com", "54321wasd");')
# connection.commit()

cursor.close()
connection.close()