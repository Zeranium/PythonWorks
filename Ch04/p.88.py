"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p88 - 추가, 삭제, 수정, 삽입 예
"""

num = ["one", "two", "three", "four"]
print(num)
print(len(num))

num.append("five")
print(num)

num.remove("five")
print(num)

num[3] = "4"
print(num)

num.insert(0, "zero")
print(num)