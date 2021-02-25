"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p138 - 함수 장식자 예
"""

def wrap(a):
    def decorated():
        print('반가워요!')
        a()
        print('잘가요!')
    return decorated

@wrap
def hello():
    print('hi ~', "홍길동")

hello()