"""
날짜 : 2021/02/21
이름 : 장한결
내용 : 교재 p101 - 단어 빈도수 구하기 예
"""

charset = ["abc", "code", "band", "band", "abc"]
wc = {}

for key in charset :
    wc[key] = wc.get(key, 0) + 1
print(wc)