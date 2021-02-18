"""
날짜 : 2021/02/18
이름 : 장한결
내용 : 교재 p52 - 문자열 처리 함수 예
"""

oneLine = "this is one line string"
print("t 글자 수 : ", oneLine.count("t"))

print("t 글자 수 : ", oneLine.startswith("this"))
print("t 글자 수 : ", oneLine.startswith("that"))

print("t 글자 수 : ", oneLine.replace("this", "that"))

multiLine = "this is\nmulti line\nstring"
sent = multiLine.split("\n")
print("문장 :", sent)

words = oneLine.split(" ")
print("단어 :", words)

sent2 = ",".join(words)
print(sent2.replace(",", " "))