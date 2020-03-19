import MySQLdb

# 建立資料庫連線
db = MySQLdb.connect(host='localhost', user='dbuser', passwd='aabb1234', db='my_demo_db', port=3306, charset='utf8')
# 建立游標
cursor = db.cursor()

# insert update delete 要加
db.autocommit(True)


try:
    sql_str = 'update product set name=\'{}\', price = {} where pid = {};'.format('nokia 6 plus', 3000, 7)

    # 執行語句
    cursor.execute(sql_str)

    # db.commit()
except Exception as err:
    print('Unable to update data to db')
    print(err)

try:
    sql_str = 'select * from product;'
    cursor.execute(sql_str)
    datarows = cursor.fetchall()

    for row in datarows:
        print(row)

except:
    print('Unable to fetch data from db')

db.close()