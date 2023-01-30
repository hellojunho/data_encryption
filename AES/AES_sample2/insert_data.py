from dao import *

sql = "INSERT INTO test_table(name, phone_num, rr_num) VALUES (%s, %s, %s)"

name = input("input name : ")
phone_num = input("input phone number : ")
rr_num = input("input resident registration number : ") # rr_num = resident_registration_number (주민등록번호)


# 주민등록번호 암호화
rr_num_dec = encrypt(rr_num)

# 암호화한 패스워드로 데이터베이스에 저장
val = (name, phone_num, rr_num_dec)
cursor.execute(sql, val)

db.commit()
db.close()

print(cursor.rowcount, "record inserted")