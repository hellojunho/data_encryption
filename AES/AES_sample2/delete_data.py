from dao import *


sql = "DELETE FROM test_table where idx=%s"

idx = int(input("input index : "))

cursor.execute(sql, idx)
db.commit()
db.close()

print(cursor.rowcount, "delete inserted")

