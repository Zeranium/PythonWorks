"""Z
날짜 : 2021/03/04
이름 : 장한결
내용 : 파이썬 SQLite CRUD 프로그래밍
"""

import sqlite3
print(sqlite3.sqlite_version_info)

conn = sqlite3.connect('./data/sqlite_db')

cur = conn.cursor()

sql ="""CREATE TABLE IF NOT EXISTS `goods`(
        `code`  INTEGER     PRIMARY KEY,
        `name`  TEXT(30)    UNIQUE NOT NULL,
        `su`    INTEGER     DEFAULT 0,
        `dan`   REAL        DEFAULT 0.0
        );
        """
cur.execute(sql)

cur.execute("INSERT INTO `goods` VALUES (1, '냉장고', 2, 8500000)")
cur.execute("INSERT INTO `goods` VALUES (2, '세탁기', 3, 5500000)")
cur.execute("INSERT INTO `goods` (`code`, `name`) VALUES (3, '전자레인지')")
cur.execute("INSERT INTO `goods`(`code`, `name`, `dan`) VALUES (4, 'HDTV', 15000000)")

code = int(input('code 입력 : '))
name = input('name 입력 : ')
su = int(input('su 입력 : '))
dan = int(input('dan 입력 : '))

sql = f"INSERT INTO `goods` VALUES({code},'{name}', {su}, {dan})"
cur.execute(sql)
conn.commit()

code = int(input('수정 code 입력 : '))
su = int(input('수정 su 입력 : '))
dan = int(input('수정 dan 입력 : '))

sql = f"UPDATE `goods` SET `su` = {su}, `dan` = {dan} WHERE `code` = {code}"
cur.execute(sql)
conn.commit()

code = int(input('삭제 code 입력 : '))
sql = f"DELETE FROM `goods` WHERE `code` = {code}"
cur.execute(sql)
conn.commit()

sql = "SELECT * FROM `goods`"
cur.execute(sql)
rows = cur.fetchall()

for row in rows:
    print(row[0], row[1], row[2], row[3])

print('검색된 레코드 수 :', len(rows))

name = input("상품명 입력 : ")
sql = f"SELECT * FROM `goods` WHERE `name` LIKE '{name}'"
cur.execute(sql)
rows = cur.fetchall()

if rows :
    for row in rows:
        print(row)
else:
    print('검색된 레코드 없음')

conn.commit()