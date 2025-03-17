#alt + shift +F10
import random

#n = int(input("숫자: "))
answer = random.randrange(1,100)

i = 0
while i < 7:
    i = i+1
    n = int(input("숫자: "))
    if n == answer:
        print("win")
        break
    elif n < answer:
        print("작음")
    elif n > answer:
        print("큼")
