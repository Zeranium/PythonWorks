"""
날짜 : 2021/03/11
이름 : 장한결
내용 : 파이썬 연습문제 9.클래스
"""

class King:

    def __init__(self, name = '태종', year = 1392):
        self.name = name
        self.year = year

    def show(self):
        print('-----------------')
        print('name :', self.name)
        print('year :', self.year)

if __name__ == '__main__':

    king1 = King()
    king2 = King('태종')
    king3 = King('세종대왕', 1418)

    king1.show()
    king2.show()
    king3.show()