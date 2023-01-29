from dao import *

sql = "INSERT INTO test_table(name, id, password) VALUES (%s, %s, %s)"

name = input("input name : ")
id = input("input id : ")
password = input("input password : ")

# 패스워드 암호화
password_enc = encrypt(password)

# 암호화한 패스워드로 데이터베이스에 저장
val = (name, id, password_enc)
cursor.execute(sql, val)

db.commit()
db.close()

print(cursor.rowcount, "record inserted")