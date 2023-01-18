# 원본 코드

# Crypto.Util.Padding을 통해서 pad와 unpad를 불러오고,
# key를 16비트로 맞추지 못했기 때문에 패딩으로 키의 길이를 맞춰줍니다.
# 인코딩은 AES_ECB 방식으로 인코딩했습니다.

from Crypto.Util.Padding import *
from Crypto.Cipher import AES
import base64

# padding 설정
BS = 16  # Block Size


# pad = lambda s: s + (BS - len(s.encode()) % BS) * chr(BS - len(s.encode()) % BS)
# unpad = lambda s: s[:-ord(s[len(s) - 1:])]


# 암호화
def encode(key, text):
    cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
    msg = cipher.encrypt(pad(text.encode(), BS))

    return msg


# 복호화
def decode(key, text):
    cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)
    msg = cipher.decrypt(text)

    return msg


def main():
    key = 'testkey'
    test = "test"
    print('original message: ', test)

    msg_enc = encode(key, test)
    print("msg_enc : ", msg_enc)

    msg_dec = decode(key, msg_enc)
    print("msg_def : ", msg_dec)

if __name__ == "__main__":
    main()
