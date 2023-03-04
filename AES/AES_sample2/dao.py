from test import *
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='password*',
    db='python',
    charset='utf8'
)

cursor = db.cursor(pymysql.cursors.DictCursor)


key = "keykey"
aes = AESCipher(key)


def main():
    sql = "select * from test_table;"

    # sql 실행
    cursor.execute(query=sql)


    # 결과 전체 가져오기
    result = cursor.fetchall()
    # result = cursor.fetchone()

    # 전체 데이터 출력
    for x in range(0, len(result)):
        print(result[x], end='\n')

    # 몇 번째 열의 요소를 가져올건지?1
    i = int(input("열 번호(idx) 입력 : ")) - 1
    e = 'rr_num'
    # print("원본 데이터 : ", result[i].get(e))
    data = result[i].get(e)
    print('암호화 : ', data)
    print('복호화 : ', decrypt(data))


def encrypt(data):
    encode = aes.encrypt(data)
    # print("암호화:", encrypt)
    return encode


def decrypt(data):
    decode = aes.decrypt(data)
    # print("복호화:", decrypt)
    return decode


if __name__ == "__main__":
    main()
