import MySQLdb

# 建立資料庫連線
db = MySQLdb.connect(host='localhost', user='dbuser', passwd='aabb1234', db='my_demo_db', port=3306, charset='utf8')

# 建立游標
cursor = db.cursor()

try:
    sql_str = 'select * from product;'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row[1])
except:
    print('unable to fetch data from db')

db.close()