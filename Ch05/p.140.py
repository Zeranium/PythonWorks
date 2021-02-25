"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p140 - 숫자 카운트 예
"""

def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)

print('n = 0 :', Counter(0))

Counter(5)