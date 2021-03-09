"""
날짜 : 2021/03/09
이름 : 장한결
내용 : 파이썬 가상 브라우저를 이용한 네이버 뉴스 수집
"""

from selenium import webdriver
from openpyxl import Workbook

browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 네이버 로그인 버튼 클릭
btn_news = browser.find_element_by_css_selector('#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(2) > a')
btn_news.click()

btn_breaking = browser.find_element_by_css_selector('#lnb > ul > li:nth-child(2) > a > span')
btn_breaking.click()

page = 2

# Excel 파일생성
workbook = Workbook()
sheet = workbook.active

while True:
    print('----------------------------------------------')
    print('page :', page-1)
    tags_title = browser.find_elements_by_css_selector('#main_content > div.list_body.newsflash_body > ul > li > dl > dt:nth-child(2) > a')

    for tit in tags_title:
        print(tit.text)
        sheet.append([tit.text.strip()])

    page_btn = "#main_content > div.paging > a:nth-child(%d)" % page
    btn_page = browser.find_element_by_css_selector(page_btn)
    btn_page.click()

    page += 1

    if page > 10:
        print('----------------------------------------------')
        break

# Excel 파일 저장
workbook.save('C:/Users/user/Desktop/News2.xlsx')

# 브라우저 종료
browser.quit()