"""
날짜 : 2021/03/04
이름 : 장한결
내용 : 파이썬 SQLite 프로그래밍
"""

import sqlite3

conn = sqlite3.connect('./data/sqlite_db')
print('DB파일 생성')

cur = conn.cursor()

sql = 'CREATE TABLE IF NOT EXISTS `test_table` ('
sql += '`name` text(10), '
sql += '`phone` text(15), '
sql += '`addr` text(50)'
sql += ');'

cur.execute(sql)

cur.execute("INSERT INTO `test_table` VALUES ('홍길동', '010-1111-1001', '서울시')")
cur.execute("INSERT INTO `test_table` VALUES ('이순신', '010-1111-1002', '해남시')")
cur.execute("INSERT INTO `test_table` VALUES ('강감찬', '010-1111-1003', '평양시')")

conn.commit()

conn.close()