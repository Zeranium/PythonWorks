# 은행계좌 클래스

class Account :
    # Attribute(변수)
    __bank = None
    __id = None
    __name = None
    __balance = 0

    # 생성자 정의
    def __init__(self, bank, id, name, balance):
        self.__bank = bank
        self.__id = id
        self.__name = name
        self.__balance = balance

    # Action(함수)
    def deposit(self, cash):
        self.__balance += cash

    def withdraw(self, cash):
        self.__balance -= cash

    def show(self):
        print("------------------------------")
        print("은행명 :", self.__bank)
        print("계좌번호 :", self.__id)
        print("입금주 :", self.__name)
        print("잔액 :", self.__balance)

    pass