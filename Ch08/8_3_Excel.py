"""
날짜 : 2021/02/24
이름 : 김철학
내용 : 파이썬 특수파일 실습 교재 p.239
"""

import pandas as pd
from openpyxl import Workbook

# CSV 특수파일 읽기
exam = pd.read_csv('C:/Users/user/Desktop/exam.csv')
print(exam)

# Excel 특수파일 읽기
exam = pd.read_excel('C:/Users/user/Desktop/exam.xlsx')
print(exam)

# Excel 특수파일 쓰기
workbook = Workbook()

# 현재 sheet 활성화
sheet = workbook.active

# 데이터 입력
sheet['C2'] = '숫자'
sheet.append([1, 2, 3])
sheet.append(['김유신', '김춘추', '장보고', '강감찬', '이순신'])
sheet.cell(5, 5, 'E열 5행 데이터')

# 파일저장
workbook.save('C:/Users/user/Desktop/Sample.xlsx')
workbook.close

print('프로그램 종료')