"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p90 - 리스트 정렬과 요소 검사 예
"""

lst = [1, 2, 3, 4]
result = lst * 2
print(result)
result.sort()
print(result)
result.sort(reverse = True)
print(result)

import random
r = []
for i in range(5) :
    r.append(random.randint(1, 5))

print(r)
if 4 in r :
    print("있음")
else:
    print("없음")