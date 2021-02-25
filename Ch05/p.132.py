"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p132 - 함수 스코프 예
"""

x = 50
def local_func(x):
    x += 50
local_func(x)
print('x =', x)

def global_func():
    global x
    x += 50

global_func()
print('x =', x)