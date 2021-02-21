"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p72 - range 클래스 예
"""

num1 = range(10)
print("num1 :", num1)

num2 = range(1, 10)
print("num2 :", num2)

num3 = range(1, 10, 2)
print("num3 :", num3)

for n in num1 :
    print(n, end=" ")
print()
for n in num2 :
    print(n, end=" ")
print()
for n in num3 :
    print(n, end=" ")