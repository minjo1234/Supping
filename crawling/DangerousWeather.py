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
    my_dict = {}  # 딕셔너리 생성
    # 페이지 열기
    driver.get(
        'https://www.weather.go.kr/w/ocean/forecast/daily-forecast.do#toggle')
#
    # toggle
    toggle_path = '//*[@id="sea-warning-now"]/div/a'
    toggle = driver.find_element(By.XPATH, toggle_path)
    print(type(toggle))
    toggle.click()

    # 결과구하기
    xpath = '//*[@id="sea-warning-now"]/div/div/div/table/thead/tr'
    xpath2 = '//*[@id="sea-warning-now"]/div/div/div/table/tbody'

    # th 요소의 개수를 구합니다.
    th = driver.find_element(By.XPATH, xpath)
    th_elements = th.find_elements(By.TAG_NAME, 'th')
    th_count = len(th_elements)

    # tr 요소의 개수를 구합니다.
    tbody = driver.find_element(
        By.XPATH, '//*[@id="sea-warning-now"]/div/div/div/table/tbody')
    tr_elements = tbody.find_elements(By.TAG_NAME, 'tr')
    tr_count = len(tr_elements)

    # dictionary key
    text_list = []
    for i in range(1, th_count + 1):
        thead = driver.find_element(By.XPATH, xpath + f'/th[{i}]')
        text_list.append(thead.text)

    # dictionary value
    for k in range(1, tr_count + 1):

        for j in range(1, th_count + 1):
            text = driver.find_element(
                By.XPATH, f'//*[@id="sea-warning-now"]/div/div/div/table/tbody/tr[{k}]/td[{j}]')
            # 1~6  8~6
            my_dict[text_list[j-1]] = text.text

    # json 폴더생성
    with open('./data/Dangerous.json', 'w', encoding='utf-8') as json_file:
        json.dump(my_dict, json_file, ensure_ascii=False, indent=4)
    time.sleep(1)
except Exception as e:
    print("Exception", e)
