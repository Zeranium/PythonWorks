"""
날짜 : 2021/02/18
이름 : 홍길동
내용 : 교재 p43 - 표준 입력장치 예
"""

# (1) 문자형 숫자 입력
num = input("숫자 입력 : ")
print("num type :", type(num))
print("num =", num)
print("num =", num*2)

# (2) 문자형 숫자를 정수형으로 별환
num1 = int(input("숫자 입력 : "))
print("num1 =", num1*2)

# (3) 문자형 숫자를 정수형으로 변환
num2 = float(input("숫자 입력 : "))
result = num1 + num2
print("result =", result)
