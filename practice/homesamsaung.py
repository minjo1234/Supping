import schedule
from bs4 import BeautifulSoup
import time
# selenium and ChormeDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

try:
    # get()
    driver.get('https://finance.naver.com/item/frgn.naver?code=005930')

    # find.element(0)
    scoreList = driver.find_element(
        By.XPATH, '//*[@id="content"]/div[2]/table[1]/tbody')

    NameXpath = '//*[@id="content"]/div[2]/table[1]/tbody/tr'
    ListName1 = driver.find_element(By.XPATH,  NameXpath + '[1]')
    ListName2 = driver.find_element(By.XPATH,  NameXpath + '[2]')

    print(type(scoreList))
    # 하나씩 리스트
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[12]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[16]

    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[5]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[6]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[7]
    # 45678 , 12~16 , 20~24 , 28~32 ,
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[20]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[28]

    # 주어진 범위를 파싱하고 리스트로 저장
    output = []
    result = []
    for i in range(4,32):
        # 단일 값 처리
        # 결과 출력
        if(  4<=  i <= 8 or 12 <= i <= 16 or 20 <= i <= 24  or 28 <= i <= 32 ):
            OneList = f'//*[@id="content"]/div[2]/table[1]/tbody/tr[{i}]'
            StockList = driver.find_element(By.XPATH, OneList)
            
        for cell in StockList.find_elements(By.TAG_NAME, 'td'):
            result.append(cell.text)

    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[1]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[2]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[3]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[4]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[5]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[6]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[7]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[8]
    # //*[@id="content"]/div[2]/table[1]/tbody/tr[4]/td[9]
   
    for i in range(len(result)):
        data = [result[i:i+9] for i in range(0, len(result), 9)]
    # 데이터를 2차원 배열로 변환
 
    # 데이터프레임 생성
    
    # 데이터프레임 생성
    df = pd.DataFrame(data, columns=['날짜', '종가', '전일비', '등락률', '거래량', '기관', '외국인', '외국인비율', '누적거래량'])


    # 데이터프레임을 CSV 파일로 저장
    df.to_csv('./data/naverScore.csv', index=False)
    time.sleep(5)
except Exception as e:
    print("Error getting", e)

# BeautifulSoup=bs4/selenium
# 8월24일에서 ~ 9월6일까지만  가져오시면 됩니다
# 삼성전자 네이버 일일 시세표 데이터 가져와서 csv,xlsx엑셀 파일로저장
# 삼성전자 다음   일일 시세표 데이터 가져와서 csv,xlsx엑셀 파일로저장
# 삼성전자 일별시세  저장을 csv이나 xlsx로 저장하기
