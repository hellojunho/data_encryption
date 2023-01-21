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
