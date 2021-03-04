"""
날짜 : 2021/03/04
이름 : 장한결
내용 : 파이썬 데이터베이스 프로그래밍
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                       user='jhg',
                       password='1234',
                       db='jhg',
                       charset='utf8')

while True:

    print('0:종료, 1:등록, 2:조회')

    result = input('입력 : ')
    if result == '0':
        print('- 프로그램이 종료되었습니다 -')
        break

    elif result == '1':
        # 사용자 등록
        uid = input('아이디 입력 : ')
        name = input('이름 입력 : ')
        hp = input('휴대폰 입력 : ')
        age = input('나이 입력 : ')

        # SQL 실행 객체 생성
        cur = conn.cursor()

        # SQL 실행
        sql = "INSERT INTO `USER1` VALUES ('%s', '%s', '%s', '%s');" % (uid, name, hp, age)
        cur.execute(sql)

        # 실행 확정
        conn.commit()


        print('- 사용자 등록 완료 -')

    elif result == '2':
        # 사용자 조회
        uid = input('조회하고 싶은 아이디 입력 : ')

        # SQL 실행 객체 생성
        cur = conn.cursor()

        # SQL 실행
        cur.execute("SELECT * FROM `USER1` WHERE `uid`= '%s';" % uid)

        # 결과 출력
        for row in cur.fetchall():
            print('----------------')
            print('아이디 :', row[0])
            print('이름 :', row[1])
            print('휴대폰 :', row[2])
            print('나이 :', row[3])
            print('----------------')

        print('- 사용자 조회 완료 -')

    else:
        print('오류: 입력값을 다시 한 번 확인해주십시오.')

conn.close()