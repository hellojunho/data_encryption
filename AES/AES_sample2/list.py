from dao import *

class list:
    def getEmps(self):
        ret = []

        sql = "select * from test_table;"
        cursor.execute(sql)

        rows = cursor.fetchall()
        for e in rows:
            # temp = {' idx': e[0], 'name': e[1], 'phone_num': e[2], 'rr_num': e[3]}
            temp = e
            ret.append(temp)

        db.commit()
        db.close()
        return ret
