"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p75 - 문장과 단어 추출 예
"""

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = []
words = []

for sen in string.split(sep = "\n") :
    sents.append(sen)
    for word in sen.split() :
        words.append(word)

print("문장 :", sents)
print("문장 수 :", len(sents))
print("단어 :", words)
print("단어 수 :", len(words))

print(string.split(sep = "\n"))