n = int(input("N의 값을 입력하세요 : "))
eori = (input("암호문을 입력하세요 : "))

d = int(input("개인키를 입력하세요 : "))

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

print("평서문 : {}".format(text))
input()
