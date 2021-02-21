"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p96 - 셋 객체 예
"""

s = {1, 3, 5, 3, 1}
print(len(s))

for d in s :
    print(d, end=" ")

print()

s2 = {3, 6}
print(s.union(s2)) # 합집합
print(s.difference(s2)) # 차집합
print(s.intersection(s2)) # 교집합

s3 = {1, 3, 5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)