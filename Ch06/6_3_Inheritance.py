"""
날짜 : 2021/02/23
이름 : 장한결
내용 : 파이썬 클래스 상속 실습하기 교재 p.163
"""

from Ch06.lib.StockAccount import *
from Ch06.lib.Student import *
from Ch06.lib.SalaryStudent import *

kb = StockAccount("KB증권", "101-451-454521", "장한결", 50000, "삼성전자", 10, 40000)
kb.deposit(50000)
kb.withdraw(4000)
kb.buy("삼성전자", 5, 45000)
kb.sell("삼성전자", 5, 50000)
kb.show()

kim = Student("김유신", 25, "해강고등학교", "인문계")
kim.hello()

lee = SalaryStudent("이순신", 31, "부경대", "경영학", "삼성전자")
lee.hello()