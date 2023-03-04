from dao import *

data = input('input: ')

encode = aes.encrypt(data)
decode = aes.decrypt(encode)

print(encode)
print(decode)