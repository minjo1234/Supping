import time
import pandas as pd
import json
# selenium and webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

try:
    # 접속
    driver.get('https://www.weather.go.kr/w/ocean/forecast/mid-term-forecast.do')

    # list 정리
    titleList = []
    WeatherList = []
    WeatherTide = []
    yangyang_dict = {}
    # title  + '오전 + 오후 따로 추가해주기'
    title = driver.find_elements(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div/section/div[2]/table/thead/tr[1]')
    titlex = driver.find_elements(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div/section/div[2]/table/thead')

    for i in title:
        ths = i.find_elements(By.TAG_NAME, 'th')
        for j in ths:
            titleList.append(j.text)
    # weather

    ContentWeather = driver.find_elements(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div/section/div[2]/table/tbody/tr[13]')
    # tide
    ContentTide = driver.find_elements(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div/section/div[2]/table/tbody/tr[14]')

    # ContentWeather
    for i in ContentWeather:
        tds = i.find_elements(By.TAG_NAME, 'td')
        for j in tds:
            WeatherList.append(j.text)
    # ContentTide
    for i in ContentTide:
        tds = i.find_elements(By.TAG_NAME, 'td')
        for j in tds:
            WeatherTide.append(j.text)
    #  dict value and keys
    for p in range(0, len(titleList)):

        if (p == 0):
            yangyang_dict[titleList[p]
                          ] = [WeatherList[p], WeatherList[p+1],  WeatherTide[p]]
        elif (1 <= p <= 5):
            yangyang_dict[titleList[p]] = [
                WeatherList[p * 2], WeatherList[p * 2 + 1],  WeatherTide[p*2-1], WeatherTide[p*2]]
        else:
            yangyang_dict[titleList[p]] = [WeatherList[p+6], WeatherTide[p+5]]
    # json 추가
    with open('./data/yangyang.json', 'w', encoding='utf8') as data:
        json.dump(yangyang_dict, data, indent=4, ensure_ascii=False)

except Exception as e:
    print('Exception', e)
