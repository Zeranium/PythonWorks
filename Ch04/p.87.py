"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p87 - 중첩 list 객체 예
"""

a = ["a", "b", "c"]
print(a)

b = [10, 20, a, 5, True, "문자열"]
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])