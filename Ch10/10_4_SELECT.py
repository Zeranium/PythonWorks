"""
날짜 : 2021/03/04
이름 : 장한결
내용 : 파이썬 삭제 실습하기
"""

import pymysql

conn = pymysql.connect(host='192.168.10.114',
                       user='jhg',
                       password='1234',
                       db='jhg',
                       charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
cur.execute("SELECT * FROM `USER1`;")

# 결과 출력
for row in cur.fetchall():
    print('----------------')
    print('아이디 :', row[0])
    print('이름 :', row[1])
    print('휴대폰 :', row[2])
    print('나이 :', row[3])
    print('----------------')

# 데이터베이스 종료
conn.close()