"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p127 - 사용자 정의함수 예
"""

# 실습 피타고라스 정의 함수 예
def pytha(s, t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2 + t**2
    print('3변의 길이 :', a, b, c)

pytha(2, 1)
# 실습 몬테카를로 시뮬레이션 함수 예