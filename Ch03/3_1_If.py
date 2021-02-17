"""
날짜 : 2021/02/17
이름 : 장한결
내용 : 파이썬 조건문 실습 교재 p.60
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print("num1은 0보다 크다")

if num1 > num2:
    print("num1은 num2보다 크다")

if num1 > 0:
    if num2 > 1:
        print("num1은 0보다 크고 num2는 1보다 크다.")

if num1 > 0 and num2 > 1:
    print("num1은 0보다 크고 num2는 1보다 크다.")

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    """조건이 참일 때"""
    print("num3는 num4보다 크다.")
else:
    """조건이 거짓일 때"""
    print("num3는 num4보다 작다.")

# if ~ elif ~ else
if num1 > num2:
    print("num1은 num2보다 크다.")
elif num2 > num3:
    print("num2는 num3보다 크다.")
elif num3 > num4:
    print("num3는 num4보다 크다.")
else:
    print("num4가 가장 크다.")

# 연습문제

"""
score = input("점수 입력: ")

score = int(score)  #숫자변환
if score > 100:
    print("잘못된 점수입니다 : 점수는 100을 넘을 수 없습니다.")
elif score >= 90 and score <= 100:
    print("당신은 A등급입니다.")
elif score >=80 and score < 90:
    print("당신은 B등급입니다.")
elif 70 <= score < 80:
    print("당신은 C등급입니다.")
elif 60 <= score < 70:
    print("당신은 D등급입니다.")
else:
    print("당신은 F등급입니다.")

print("score :", score)
"""

# 교재 p.63 삼항조건문
# (1) 일반 조건문
num = 9 # 초기화
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
print("result =", result)

# (2) 3항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
"""
result2 = num * 2 if num >= 5 else num + 2
print("result2 =", result2)
"""

result2 = "True" if num <= 8 else "False"
print(result2)

score = int(input("점수 입력: "))
grade = ""

if 85 <= score <= 100:
    grade = "우수"
elif 70 <= score < 85:
    grade = "보통"
else:
    grade = "저조"

print("당신의 점수는 %d점이고, 당신의 등급은 '%s'입니다" % (score, grade))