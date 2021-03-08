"""
날짜 : 2021/03/08
이름 : 장한결
내용 : 파이썬 네이버 뉴스 크롤링 실습하기
"""

import requests as rq
from bs4 import BeautifulSoup as bs
from openpyxl import Workbook

"""
resp = rq.get('https://news.naver.com/', headers={'User-Agent': 'Mozilla/5.0'})
#print(resp.text)

dom = bs(resp.text, 'html.parser')
hl = dom.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')

for a in hl:
    print(a.text.strip())
"""
page = 1

# Excel 파일생성
workbook = Workbook()
sheet = workbook.active


while True:
    print('page :', page)
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date=20210308&page=' + str(page)
    resp = rq.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    dom = bs(resp .text, 'html.parser')
    hl = dom.select('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2) > a')

    for a in hl:
        # print(a.text.strip())
        sheet.append([a.text.strip()])

    page += 1

    if page > 10:
        break

# Excel 파일 저장
workbook.save('C:/Users/user/Desktop/News.xlsx')