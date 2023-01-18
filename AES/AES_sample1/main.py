from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64

# padding 설정
BS = 16 # Block Size
# pad = lambda s: s + (BS - len(s.encode()) % BS) * chr(BS - len(s.encode()) % BS)
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]

# 변수 설정

key = 'testkey'
info1 = input("input text1>> ")
info2 = input("input text2>> ")

print("-"*100)

# 암호화
cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)

print('Info1 : ', info1)
msg1 = cipher.encrypt(pad(info1.encode(), BS))
print('msg', msg1)
m1 = base64.b64encode(msg1)
print('base64', m1)
msg_dec = cipher.decrypt(base64.b64decode(m1))
print('msg_dec', msg_dec)

print('-'*100)

print('Info2 : ', info2)

msg2 = cipher.encrypt(pad(info2.encode(), BS))
print('msg', msg2)
m2 = base64.b64encode(msg2)
print('base64', m2)
msg_dec = cipher.decrypt(base64.b64decode(m2))
print('msg_dec', msg_dec)

print('-'*100)