"""
날짜 : 2021/03/04
이름 : 장한결
내용 : 파이썬 삭제 실습하기
"""

import pymysql

# 데이터베이스 접속

conn = pymysql.connect(host='192.168.10.114',
                       user='jhg',
                       password='1234',
                       db='jhg',
                       charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()

# SQL 실행
sql = "DELETE FROM `USER1` WHERE `uid`='p101';"
cur.execute(sql)

# 실행 확정
conn.commit()

# 데이터베이스 접속 종료
conn.close()

print('- DELETE 완료 -')