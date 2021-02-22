"""
날짜 : 2021/02/22
이름 : 장한결
내용 : 파이썬 모듈 패키지 실습하기 p.114
"""

import Ch05.lib.calc as cal

rs1 = cal.plus(1, 2)
rs2 = cal.minus(1, 2)
rs3 = cal.multi(1, 2)
rs4 = cal.div(1, 2)

print("rs1 :", rs1)
print("rs2 :", rs2)
print("rs3 :", rs3)
print("rs4 :", rs4)

#################################

from Ch05.lib.calc import *

r1 = plus(1, 2)
r2 = minus(1, 2)
r3 = multi(1, 2)
r4 = div(1, 2)

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)
print("r4 :", r4)

#################################

from random import *
print(randint(1, 100))