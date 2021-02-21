"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p73 - list 자료구조 예
"""
import random

lst = []
for i in range(10) :
    r = random.randint(1, 10)
    lst.append(r)

print("lst =", lst)

for i in range(10) :
    print(lst[i] * 0.25)