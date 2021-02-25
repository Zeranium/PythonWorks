"""
날짜 : 0000/00/00
이름 : 홍길동
내용 : 교재 p161 - 캡슐화 예
"""

class Account:
    __balance = 0
    __accName = None
    __accNo = None

    def __init__(self, bal, name, no):
        self.__balance = bal
        self.__accName = name
        self.__accNo = no

    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    def deposit(self, money):
        if money < 0:
            print('금액확인')
            return
        self.__balance += money

    def withdraw(self, money):
        if self.__balance < money:
            print('잔액부족')
            return
        self.__balance -= money

acc = Account(1000, '홍길동', '125-152-4125-41')

bal = acc.getBalance()
print(bal)

acc.deposit(10000)
bal = acc.getBalance()
print(bal)