"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p131 - 람다 함수 예
"""

def Adder(x, y):
    add = x + y
    return add

print('add =', Adder(10, 20))

print('add =', (lambda x, y:  x + y)(10, 20))