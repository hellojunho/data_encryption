from dao import *


sql = """create table test_table(
	        idx int not null auto_increment primary key,
	        name varchar(256),
	        id varchar(256),
	        password varchar(256)
);"""

cursor.execute(sql)
db.commit()
