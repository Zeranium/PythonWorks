"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p61 - 단일 조건문
"""

# 단일 조건문 형식 1 예문
var = 10
if var >= 5:
    print("var =", var)
    print("var는 5보다 크다.")
    print("조건이 참인 경우 실행")

print("항상 실행")

# 단일 조건문 형식 2 예문
score = int(input("점수 입력 : "))
if 85 <= score <= 100:
    print("우수")
else:
    if 70 <= score < 85:
        print("보통")
    else:
        print("저조")