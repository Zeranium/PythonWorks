# 은행계좌 클래스

class Account :
    # Attribute(변수)
    bank = None
    id = None
    name = None
    balance = 0

    # Action(함수)
    def deposit(self, cash):
        self.balance += cash

    def withdraw(self, cash):
        self.balance -= cash

    def show(self):
        print("------------------------------")
        print("은행명 :", self.bank)
        print("계좌번호 :", self.id)
        print("입금주 :", self.name)
        print("잔액 :", self.balance)

    pass