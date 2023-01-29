from dao import *

class list:
    def getEmps(self):
        ret = []

        sql = "select * from test_table;"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for e in rows:
            temp = {'index': e[0], 'name': e[1], 'id': e[2], 'password': e[3]}
            ret.append(temp)

        db.commit()
        db.close()
        return ret
