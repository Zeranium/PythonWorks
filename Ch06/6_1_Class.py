"""
날짜 : 2021/02/23
이름 : 장한결
내용 : 파이썬 클래스 실습하기 p.148
"""

from Ch06.lib.Account import Account

# Account 객체생성
kb = Account()

kb.bank = "국민은행"
kb.id = '654202-04-022407'
kb.name = "장한결"
kb.balance = 10000

# 객체 기능 활용
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

# 객체생성 및 초기화
wr = Account()
wr.bank = "우리은행"
wr.id = "110-361-485645"
wr.name = "지대선"
wr.balance = 30000

# 객체 기능 활용
wr.deposit(10000)
wr.withdraw(20000)
wr.show()