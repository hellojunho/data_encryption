from dao import *


# sql = """create table test_table(
# 	        idx int not null auto_increment primary key,
# 	        name varchar(256),
# 	        id varchar(256),
# 	        password varchar(256)
# );"""

sql = '''
    create table test_table(
        idx int not null auto_increment primary key, 
        name varchar(80), 
        phone_num varchar(80), 
        rr_num varchar(80)
    )
'''

cursor.execute(sql)
db.commit()
