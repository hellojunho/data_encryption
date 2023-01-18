# 암호화 알고리즘

## AES
AES 암호화 알고리즘은 1급 비밀에 사용할 수 있도록 승인된 유일하게 공개된 암호화 알고리즘임.  
AES는 `레인달 알고리즘`을 가리킴.  
블럭의 크기가 128비트이고, 암호화 키의 길이가 128, 192, 256 비트인 3가지 종류가 표준.  
AES-128, AES-192, AES-256

128비트(16바이트)가 안되는 키의 경우 `패딩`이라는 의미없는 값으로 채우는 과정이 필요함.  
이메일의 경우에는 base64로 한 번 더 인코딩을 함.  
통신과정에서 바이너리 데이터의 손실을 막기 위해서..  

### AES_sample1

[Sample1](https://dorudoru.tistory.com/2258#2.%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%20AES%EC%95%94%ED%98%B8%ED%99%94%20%EC%83%98%ED%94%8C%EC%BD%94%EB%93%9C)

`Crypto.Util.Padding`을 통해 pad와 unpad를 불러옴.  
키를 16바이트로 맞추지 못해서 패딩으로 키의 길이를 맞춰주는 작업을 함.  
인코딩은 AES_ECB 방식으로 진행함.  

[main.py]  
```angular2html
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64

#padding 설정
BS = 16
#pad = lambda s: s + (BS - len(s.encode()) % BS) * chr(BS - len(s.encode()) % BS)
#unpad = lambda s: s[:-ord(s[len(s) - 1:])]

#변수 설정

key = 'testkey'
ori = 'test@doru.com'
print('ori',ori)

#암호화
cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
msg = cipher.encrypt(pad(ori.encode(), BS))
print('msg',msg)
m2 = base64.b64encode(msg)
print('base64',m2)
```

### AES_sample2
[Sample2](https://openuiz.tistory.com/121)  



[test.py]  
```angular2html
from AES_sample2.test import *
import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='mysql_password*',
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
    for x in range(0,len(result)):
        print(result[x], end='\n')

    # 몇 번째 열의 요소를 가져올건지?
    i = int(input("열 번호(idx) 입력 : ")) - 1
    e = input('데이터 입력(name, id, password) : ')
    print("원본 데이터 : ", result[i].get(e))

    data = result[i].get(e)
    # data = input("문장 입력 : ")
    print('암호화 : ', encrypt(data))
    print('복호화 : ', decrypt(encrypt(data)))


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
```  

## RSA

[app.py]  
```angular2html
import random

p = 13
q = 29
# p = random.randint(0, 20)
# q = random.randint(20, 40)
n = p * q
tot = (p - 1) * (q - 1)


# 최대공약수 구하는 거
def gcd(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


# 공개키
def publickey():
    global tot
    e = 2
    while e < tot and gcd(e, tot) != 1:
        e += 1
    return e


# 개인키
def privatekey():
    global e
    global tot
    d = 1
    while (publickey() * d) % tot != 1 or d == publickey():
        d += 1
    return d


ori = (input("문자열 입력(영어 문자열) : "))
oris = list(ori)
orior = []
eori = []

etext = ""
for orisc in range(0, len(oris)):
    orior.append(ord(oris[orisc]))
for oriorc in range(0, len(orior)):
    eori.append(((orior[oriorc] ** publickey()) % n))

for eoric in range(0, len(eori)):
    etext += (chr(eori[eoric]))

print("암호문(NUMBER) : {}".format(eori))
print("암호문(ASCII) : {}".format(etext))
print("N : {}".format(n))
print("공개키 : {}".format(publickey()))
print("개인키 : {}".format(privatekey()))

eori = etext

d = privatekey()

eoris = list(eori)
eroiso = []
eroisor = []
eroar = []
text = ""

for eorisc in range(0, len(eoris)):
    eroiso.append(ord(eoris[eorisc]))

for eroisoc in range(0, len(eroiso)):
    eroisor.append((eroiso[eroisoc] ** d) % n)

for eroisorc in range(0, len(eroisor)):
    eroar.append(chr(eroisor[eroisorc]))

for eroarc in range(0, len(eroar)):
    text += eroar[eroarc]

open_key = int(input("공개키 입력 : "))
private_key = int(input("개인키 입력 : "))

if open_key == publickey() and private_key == privatekey():
    print("복호화 한 결과 : {}".format(text))
    input()
else:
    print("키 오류")
    exit()
```