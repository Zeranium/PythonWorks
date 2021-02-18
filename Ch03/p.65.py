"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p65 - while 반복문 예
"""

cnt = tot = 0

while cnt < 5:
    cnt += 1
    tot += cnt
    print(cnt, tot)

cnt = tot = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print(tot)
print(dataset)