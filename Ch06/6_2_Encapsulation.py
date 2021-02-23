"""
날짜 : 2021/02/23
이름 : 장한결
내용 : 파이썬 객체지향 캡슐화 실습하기 교재 p.161
"""

from Ch06.lib.Account import Account
from Ch06.lib.Calc import Calc
from Ch06.lib.Person import Person

kb = Account("국민은행", "664121-04-454507", "장한결", 10000)

"""
kb.bank = "국민은행"
kb.id = "664121-04-454507"
kb.name = "장한결"
kb.balance = 10000
"""

kb.deposit(20000)
kb.withdraw(3000)
# kb.balance -= 1
kb.show()

wr = Account("우리은행", "110-364-457545", "지대선", 20000)

wr.deposit(30000)
wr.withdraw(5000)
wr.show()

# 연습문제
cal = Calc()

r1 = cal.plus(1, 2)
r2 = cal.minus(1, 2)
r3 = cal.multi(2, 3)
r4 = cal.div(4, 2)

print("r1 :", r1)
print("r2 :", r2)
print("r3 :", r3)
print("r4 :", r4)

kim = Person("김유신", 25)
kim.hello()

lee = Person("이순신", 35)
lee.hello()

