import pandas as pd
import time
import numpy as np

from selenium import webdriver  # 웹 브라우저 식별
from selenium.webdriver.common.by import By  # 웹 요소 식별
# 크롬 브라우저를 자동으로 설치해준다 .
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()  # webdriver option 설정
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # logging - 기록설정
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://finance.daum.net/quotes/A005930#current/quote')
    result = []
    data = []

    for i in range(1, 11):
        xpath = f'//*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[{i}]'
        ScoreList = driver.find_elements(By.XPATH, xpath)
        for j in range(len(ScoreList)):
            td_elements = ScoreList[j].find_elements(By.TAG_NAME, 'td')
            for td in td_elements:
                result.append(td.text)

    for i in range(len(result)):
        data = [result[i:i+8] for i in range(0, len(result), 8)]

    df = pd.DataFrame(
        data, columns=['날짜', '종가', '전일비', '등락률', '거래량', '기관',  '외국인비율', '누적거래량'])

    # 데이터프레임을 CSV 파일로 저장
    df.to_csv('./data/daumScore.csv', index=False)
    time.sleep(1)

except Exception as e:
    print("Error", e)

# 규칙성
   # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[1]
    # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[2]
    # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[5]
    # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[5]
    # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[6]
    # //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[10]
    #
# //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody/tr[5]
#  //*[@id="boxDayHistory"]/div/div[2]/div/table/tbody
