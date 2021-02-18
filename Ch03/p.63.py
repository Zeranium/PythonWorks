"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p63 - 삼항 조건문 예
"""

num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2

print(result)

result2 = num *2 if num >= 5 else num +2
print(result2)