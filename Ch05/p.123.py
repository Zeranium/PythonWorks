"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p123 - 사용자 정의함수 예
"""

def s():
    print('인수가 없는 함수')
    print('userFunc1')

s()

def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z =',z)

userFunc2(2,3)

def userFunc3(x, y):
    print('userFunc3')
    tot = x+y
    sub = x-y
    mul = x*y
    div = x/y

    return tot, sub, mul, div

t, s, m, d = userFunc3(10, 20)
print(t)
print(s)
print(m)
print(d)