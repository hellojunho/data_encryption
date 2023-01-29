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

sql = "INSERT INTO test_table(name, id, password) VALUES (%s, %s, %s)"

name = input("input name : ")
id = input("input id : ")
password = input("input password : ")

val = (name, id, password)
mycursor.execute(sql, val)

db.commit()
db.close()

print(mycursor.rowcount, "record inserted")