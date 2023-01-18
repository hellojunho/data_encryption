# 데이터가 이메일인 경우와 아닌 경우를 나눠서 암호화 진행하려고 테스트중

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64


# padding 설정
BS = 16  # Block Size = 16 byte

# 키 설정
key = 'testkey'
cipher = AES.new(pad(key.encode(), BS), AES.MODE_ECB)


def main():
    # msg = input("input text>> ")
    # print('1차 암호화 : ', encode(msg))
    # print('2차 암호화 : ', encode_email(encode(msg)))
    # print('최종 복호화 : ', decode_email(encode_email(encode(msg))))
    msg2 = input("input text>> ")
    print('1차 암호화 : ', encode(msg2))
    print('최종 복호화 : ', decode(encode(msg2)))


# 암호화
def encode(text):
    msg1 = cipher.encrypt(pad(text.encode(), BS))
    return msg1


def decode(text):
    msg2 = cipher.decrypt(text)
    return msg2


# 이메일인 경우 암호화
def encode_email(text):
    msg_email = base64.b64encode(text)
    # print("이메일 인코딩: ", msg_email)
    return msg_email


# 이메일인 경우 복호화
def decode_email(text):
    msg_dec = cipher.decrypt(base64.b64decode(text))
    # print('msg_dec', msg_dec)
    return msg_dec


if __name__ == "__main__":
    main()
