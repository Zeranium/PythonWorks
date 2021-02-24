"""
날짜 : 2021/02/24
이름 : 장한결
내용 : 파이썬 입출력 실습하기 교재 p.217
"""

# 파일 읽기

file = open('C:/Users/user/Desktop/Sample.txt', 'r', encoding='UTF8')
line = file.readline()

print('line :', line)
file.close()

# 멀티라인 파일 읽기
file = open('C:/Users/user/Desktop/Sample.txt', 'r', encoding='UTF8')

while True:
    line = file.read()

    if not line:
        break

    print(line)

file.close()

# 파일 쓰기
Sample2 = open('C:/Users/user/Desktop/Sample2.txt', 'w', encoding='UTF8')
Sample2.write('안녕하세요.\n')
Sample2.write('반갑습니다.\n')
Sample2.write('감사합니다.')
Sample2.close()

# 구구단 쓰기
gugudan = open('C:/Users/user/Desktop/gugudan.txt', 'w', encoding='UTF8')

for i in range(2, 10):
    gugudan.write('\n=========%d단=========\n' % i)
    for j in range(1, 10):
        k = i + j
        gugudan.write('%d X %d = %d\n' % (i, j, k))