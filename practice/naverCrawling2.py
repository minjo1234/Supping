
import pandas as pd
import time
import datetime
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

import schedule
from bs4 import BeautifulSoup
import requests


from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# homesamsungNAVER.py
# BeautifulSoup=bs4/selenium
# 8월24일에서 ~ 9월6일까지만  가져오시면 됩니다
# 삼성전자 네이버 일일 시세표 데이터 가져와서 csv,xlsx엑셀 파일로저장
# 삼성전자 다음   일일 시세표 데이터 가져와서 csv,xlsx엑셀 파일로저장

try:
    code = '005930'  # 삼성전자코드
    url = f'https://finance.naver.com/item/sise_day.naver?code={code}'  # url접근
    # 크롤링, headers 반드시 요구함
    req = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    html = BeautifulSoup(req.text, 'html.parser')  # html 내용 가져오기
    df = None

    pgrr = html.find('td', class_='pgRR')  # 페이지 정보 들고있는 td 클래스이름 찾아서 기입
    print(pgrr.a['href'])  # /item/sise_day.naver?code=005930&page=683
    page_number = pgrr.a['href'].split('=')  # 마지막 페이지 추출을 위하여 나눔
    print(page_number)  # ['/item/sise_day.naver?code', '005930&page', '683']
    last_page = page_number[-1]  # 제일 끝에 마지막 페이지 수가 있으니 -1로 마지막 꺼 가져옴
    print(last_page)  # 683 string
    headers = {'User-Agent': 'Mozilla/5.0'}

    # for page in range(1):  # 끝까지 불러올시 last_page 사용 int(last_page)+1
    #     req = requests.get(f'{url}&page={page}', headers={
    #                        'User-agent': 'Mozilla/5.0'})
    #     df = pd.concat(
    #         [df, pd.read_html(req.text, encoding='utf-8')[0]], ignore_index=True)

    # df.dropna(inplace=True)  # 데이터 없는 행 삭제
    # df.reset_index(drop=True, inplace=True)  # 삭제 이후 재정렬
    # # encoding~ 테이블 종목 한글 깨짐 방지
    # df.to_csv('./data/samsungDayPrice.csv', encoding='utf-8-sig')
    # print(df)

    time.sleep(5)
    driver.close()
except Exception as ex:
    print('에러이유 ', ex)
