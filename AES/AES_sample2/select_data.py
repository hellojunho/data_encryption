from dao import *

sql = "select * from test_table;"

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='password*',
    db='python',
    charset='utf8'
)

# sql 실행
cursor.execute(query=sql)


# 결과 전체 가져오기
result = cursor.fetchall()
# result = cursor.fetchone()

# 전체 데이터 출력
for x in range(0, len(result)):
    print(result[x], end='\n')

db.close()
