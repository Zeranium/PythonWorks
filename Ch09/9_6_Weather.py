"""
날짜 : 2021/03/09
이름 : 장한결
내용 : 파이썬 셀레늄을 활용한 날씨 크롤링 실습
"""

from selenium import webdriver
import pymysql

# 가상브라우저 실행
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

trs = browser.find_elements_by_css_selector('#weather_table > tbody > tr')

# 데이터베이스 접속
conn = pymysql.connect(host     = '192.168.10.114',
                       user     = 'jhg',
                       password = '1234',
                       db       = 'jhg',
                       charset  = 'utf8')

cursor = conn.cursor()

for tr in trs:
    city     = tr.find_element_by_css_selector('td > a').text
    visible  = tr.find_element_by_css_selector('td:nth-child(3)').text
    temp     = tr.find_element_by_css_selector('td:nth-child(6)').text
    dew      = tr.find_element_by_css_selector('td:nth-child(7)').text
    feel     = tr.find_element_by_css_selector('td:nth-child(8)').text
    humidity = tr.find_element_by_css_selector('td:nth-child(11)').text
    wind_dir = tr.find_element_by_css_selector('td:nth-child(12)').text
    wind_spd = tr.find_element_by_css_selector('td:nth-child(13)').text
    sea      = tr.find_element_by_css_selector('td:nth-child(14)').text

    # SQL 실행
    sql = "INSERT INTO `WEATHER` SET "
    sql += "`city`='"+city+"',"
    sql += "`visible`='"+visible+"',"
    sql += "`temp`='"+temp+"',"
    sql += "`dew`='"+dew+"',"
    sql += "`feel`='"+feel+"',"
    sql += "`humidity`='"+humidity+"',"
    sql += "`wind_dir`='"+wind_dir+"',"
    sql += "`wind_spd`='"+wind_spd+"',"
    sql += "`sea`='"+sea+"',"
    sql += "`rdate`= NOW();"

    cursor.execute(sql)
    conn.commit()

    print('수집 중')

    #print(city, visible, temp, dew, feel, humidity, wind_dir, wind_spd, sea)

# 데이터베이스 종료
conn.close()

# 브라우저 종료
browser.quit()

print('수집 완료!')