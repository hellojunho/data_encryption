from test import *
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='password',
    db='python',
    charset='utf8'
)

# cursor = db.cursor(pymysql.cursors.DictCursor)
cursor = db.cursor()

sql = "select * from test_table;"

# sql 실행
cursor.execute(query=sql)


# 결과 전체 가져오기
result = cursor.fetchall()
# result = cursor.fetchone()

# 전체 데이터 출력
for x in range(0,len(result)):
    print(result[x], end='\n')

db.close()
