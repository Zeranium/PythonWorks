"""
날짜 : 2021/03/09
이름 : 장한결
내용 : 파이썬 크롤링 셀레니움 실습하기
"""

from selenium import webdriver

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')

# 네이버 이동
browser.get('http://naver.com')

# 네이버 로그인 버튼 클릭
btn_login = browser.find_element_by_css_selector('#account > a')
btn_login.click()

# 네이버 아이디, 비밀번호 입력
input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_id('pw')
btn_login2 = browser.find_element_by_css_selector('#log\.login')

input_id.send_keys('')
input_pw.send_keys('')
btn_login2.click()