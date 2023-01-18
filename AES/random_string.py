import string
import random

letters_set = string.ascii_letters
random_list = random.sample(letters_set,16)
result = ''.join(random_list)
print("랜덤 문자열 : ", result)
