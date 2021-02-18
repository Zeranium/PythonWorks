"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p47 - 외부상수 출력 예
"""
name = "장한결"
age = 29
price = 12.5678

# 외부 상수 인수
print("이름 : {}, 나이 : {}, data = {}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data = {2}".format(age, name, price))

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query)