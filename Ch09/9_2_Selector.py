"""
날짜 : 2021/03/08
이름 : 장한결
내용 : 파이썬 웹 Selector 실습하기
"""

import requests as rq
from bs4 import BeautifulSoup as bs

# 페이지 요청
resp = rq.get('http://chhak.kr/py/test1.html')
resp.encoding = 'utf-8'
print(resp.text)

# 파싱
dom = bs(resp.text, 'html.parser')

tag_tit = dom.html.body.h1
tag_txt = dom.select_one('#txt')
tag_li1 = dom.select_one('ul > li:nth-child(1)')
tag_li2 = dom.select_one('ul > li:nth-child(2)')
tag_li3 = dom.select_one('ul > li:nth-child(3)')
tag_li4 = dom.select_one('ul > li:nth-child(4)')
tag_li5 = dom.select_one('ul > li:last-child')
tag_lis = dom.select('ul > li')

print(tag_tit.text)
print(tag_txt.text)
print(tag_li1.text)
print(tag_li2.text)
print(tag_li3.text)
print(tag_li4.text)
print(tag_li5.text)
print(tag_lis)

for li in tag_lis:
    print(li.text)