import mysql.connector

connection = mysql.connector.connect(host = 'localhost', 
                                     port = '3306',
                                     user = 'root',
                                     password = 'oyangwei7365o',
                                     database = 'db') #加這一行代表直接使用這個資料庫

cursor = connection.cursor()

# 取得表格所有資料
cursor.execute('SELECT * FROM `account`')

records = cursor.fetchall()
for r in records:
    print(r)

cursor.close()
connection.close()