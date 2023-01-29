import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='password',
    db='python',
    charset='utf8'
)


mycursor = db.cursor()

sql = "DELETE FROM test_table where idx=%s"

idx = int(input("input index : "))

mycursor.execute(sql, idx)
db.commit()
db.close()

print(mycursor.rowcount, "delete inserted")

