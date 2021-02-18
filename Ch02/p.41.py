"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p41 - 대입연산자
"""

# (1) 변수에 값 할당(=)
i = tot = 10 # i - 10; tot = 10
i += 1
tot += i
print(i, tot)

# 같은 줄에 중복 출력
print("출력1", end=", ")
print("출력2")

v1, v2 = 100, 200
# (2) 변수 교체
v2, v1 = v1, v2
print(v1, v2)

# (3) 패킹(packing) 할당
lst = [1, 2, 3, 4, 5, 6]
first, second, *third = lst
print(first, second, third)

*v3, v4, v5 = lst
print(v3, v4, v5)