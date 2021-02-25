"""
날짜 : 2021/02/25
이름 : 장한결
내용 : 교재 p137 - 획득자와 지정자 예
"""

"""
그렇게 노래방으로 가서 그녀가 좋아하는 노랠 해
무심한 척 준비 안 한 척 노랠 불렀네
그렇게 내가 노랠 부른 뒤 그녀의 반응을 상상하고
좀 더 잘 불러볼 걸, 노랠 불러 버렸네
"""

def main_func(num):
    num_val = num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value
    return getter, setter

getter, setter = main_func(100)

print('num =', getter())

setter(200)
print('num =', getter())