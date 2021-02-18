"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p67 - random 관련 함수 1 예
"""

import random

r = random.random()
rr = int(float(format(r, "2.2f"))*100)
print(type(rr))
print(rr)

cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.001:
        break
    else:
        cnt += 1

print("난수 개수 =", cnt)