import pymysql

# MySQL 連線資訊
MYSQL_USER = "root"
MYSQL_PASSWORD = "oyangwei7365o"
MYSQL_HOST = "db"
MYSQL_PORT = 3306
MYSQL_DB = "db"

# 建立 MySQL 連線
def get_connection():
    connection = pymysql.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DB,
        port = MYSQL_PORT,
        cursorclass = pymysql.cursors.DictCursor  # 回傳字典格式的資料
    )
    return connection

# 負責連接資料庫