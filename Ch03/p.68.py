"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p68 - random 관련 함수 2 예
"""

import random
r = random.random()

names = ["홍길동", "이순신", "유관순"]
print(names)
print(names[2])

if "유관순" in names :
    print("유관순 있음")
else :
    print("유관순 없음")

idx = random.randint(0, 2)
print(names[idx])