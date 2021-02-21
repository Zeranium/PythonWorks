"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p89 - 추가, 삭제, 수정, 삽입 예
"""

x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
print(z)

x.extend(y)
print(x)
print("len(x) :", len(x))

x.append(y)
print(x)
print("len(x) :", len(x))

lst = [1, 2, 3, 4]
result = lst * 2
print(result)