"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p99 - 딕트 객체 예
"""

dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

person = {"name" : "홍길동", "age" : 35, "address" : "서울시"}
print(person)
print(person["name"])
print(type(dic), type(person))

person["age"] = 45
print(person)

del person["address"]
print(person)

person["pay"] = 350
print(person)