import pandas as pd

import schedule  # pip install schedule
from bs4 import BeautifulSoup as BeautifulSoup  # pip install bs4
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

x_val = []
y_val = []
count = 0
total = 1

url = 'https://finance.daum.net/quotes/A005930#home'
driver.get(url)
time.sleep(5)


def check():
    global x_val
    global y_val
    global count
    global count

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    test1 = soup.select(
        '#boxSummary > div > span:nth-child(1) > span.currentB > span.numB.down > strong')  # 삼성전자주식값 70,700
    msg = str(test1)
    print('주식 가격 = ', msg)


check()  # 함수호출


pathxls = './data/samsung.xls'
driver.close()
