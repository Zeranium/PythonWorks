"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p50 - 슬라이싱 예
"""

oneLine = "this is one line string"
print("문자열 길이 :",len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

print(oneLine[-11:])