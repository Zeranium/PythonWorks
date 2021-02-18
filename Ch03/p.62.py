"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p62 - 중첩 조건문 예
"""

score = int(input("점수 입력 : "))
grade = ""

if score >= 85 and score <= 100:
    grade = "우수"
elif score >= 70:
    grade = "보통"
else:
    grade = "저조"

print(f"당신의 점수는 {score}점이며 등급은 '{grade}'입니다.")