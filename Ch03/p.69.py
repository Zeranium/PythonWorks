"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p69 - break, continue 예
"""

i = 0
while i < 10 :
    i += 1
    if i == 3 :
        continue
    if i == 6 :
        break
    print(i, end = " ")