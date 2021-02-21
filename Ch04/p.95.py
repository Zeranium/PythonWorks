"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p95 - 튜플 관련 함수 예
"""

lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))