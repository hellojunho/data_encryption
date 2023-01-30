# AES_sample1

AES_sample1은 이메일 정보를 암호화함.  
이메일의 경우에는 `base64`방식을 통해 암호화를 한 번 더 거쳐야 함.  
결론적으로 `문자열 암호화 -> 이메일 암호화 -> 복호화`의 과정을 거침.  



### 디렉토리 구조
```python
AES_sample1
    - aes_sample.py
    - encoding.py
    - encrypted.py
    - final_test.py
    - main.py
```

### 출력 결과

[encoding.py]  
```python
original message:  test
msg_enc :  b'E\xc3\x02\x92M\x91\xb9\x06 \x8c\xf6\xb8\xf6\xd1|\xbd'
msg_def :  b'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'

```

<br>

[main.py]  
```python
input text1>> test
input text2>> test2
----------------------------------------------------------------------------------------------------
Info1 :  test
msg b'E\xc3\x02\x92M\x91\xb9\x06 \x8c\xf6\xb8\xf6\xd1|\xbd'
base64 b'RcMCkk2RuQYgjPa49tF8vQ=='
msg_dec b'test\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'
----------------------------------------------------------------------------------------------------
Info2 :  test2
msg b'\xc1Y\x03I\xf5`\xb6d<\xdcUW\xce\xe7\x1c\xa8'
base64 b'wVkDSfVgtmQ83FVXzuccqA=='
msg_dec b'test2\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'
----------------------------------------------------------------------------------------------------
```  