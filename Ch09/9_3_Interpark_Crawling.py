"""
날짜 : 2021/03/08
이름 : 장한결
내용 : 파이썬 인터파크항공 크롤링 실습하기
"""

import requests as rq
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

day = 10


# Excel 파일생성
workbook = Workbook()
sheet = workbook.active


while True:
    print('day :', day)
    url = 'http://domair.interpark.com/dom/main.do?trip=OW&dep=GMP&arr=PUS&dep2=PUS&arr2=GMP&depdate=202103%d&retdate=20210310&adt=1&chd=0&inf=0&mbn=tour_main&mln=search_domair0#anchor-list' % day
    resp = rq.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    dom = bs(resp .text, 'html.parser')
    hl = dom.select('#availDepResult > table > tbody > tr > td')

    for a in hl:
        print(a.text.strip())
        # sheet.append([a.text.strip()])

    day += 1

    if day > 20:
        break


# Excel 파일 저장
workbook.save('C:/Users/user/Desktop/Fare.xlsx')
