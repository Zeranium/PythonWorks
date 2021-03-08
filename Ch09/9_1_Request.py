"""
날짜 : 2021/03/08
이름 : 장한결
내용 : 파이썬 웹 Request 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs

# 네이버 요청
resp = req.get('https://www.naver.com')
#print(resp.text)

# 파싱(HTML문서에서 특정 데이터 추출)
dom = bs(resp.text, 'html.parser')
tag_a = dom.select_one('#yna_rolling > div:nth-child(8) > a')
#print(tag_a.text)

resp2 = req.get('https://www.koreanair.com/booking/select-flight')

dom2 = bs(resp2.text, 'html.parser')
tag_a2 = dom2.select_one('#\30 bca5cab-91a7-4e76-8d97-dc350631427dDomesticAirBounds > div > div.flight__list.-type2.ng-star-inserted > ul > li:nth-child(2) > div.flight__contents > div > div:nth-child(1) > div > div > span.flight__price > span')