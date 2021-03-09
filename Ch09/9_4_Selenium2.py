"""
날짜 : 2021/03/09
이름 : 장한결
내용 : 파이썬 크롤링 셀레니움 실습하기
"""

from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://domair.interpark.com/dom/main.do?trip=OW&dep=GMP&arr=PUS&dep2=PUS&arr2=GMP&depdate=20210309&retdate=20210311&adt=1&chd=0&inf=0&mbn=tour_main&mln=search_domair0#anchor-list')

# 네이버 로그인 버튼 클릭
input_arr = browser.find_element_by_css_selector('#si_depListT')
btn_login.click()


