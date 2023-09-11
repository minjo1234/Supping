import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import json
import re
# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)


try:
    # /html/body/div[2]/section/div/div[2]/div[2]/div/div[2]/a
    # 버튼 웹 요소 찾기
    # midterm
    url = "https://www.weather.go.kr/w/wnuri-sfct/today/mid-term.do?topArea=12C20000&midArea=12C20100&btmArea=12C20100&unit=m%2Fs"
    response = requests.get(url)

    # HTTP 응답 코드를 확인하여 요청이 성공했는지 확인할 수 있습니다.
    if response.status_code == 200:
        page_content = response.text
    else:
        print("웹 페이지에 접근할 수 없습니다.")
        exit()
    soup = BeautifulSoup(page_content, "html.parser")
    # h3 태그 찾기
    h3_tag = soup.find('h3')

    # strong 태그 찾기
    title = h3_tag.find('strong').text
    print("페이지 제목:", title)
    # ul , li
    content = soup.find('ul')
    # thead , tbody  caption
    wave_heights = content.find_all('li')
    first_li = wave_heights[0]
    second_li = wave_heights[1]
    contentList = []
    for i in wave_heights:
        contentList.append(i.text)

    # print(contentList)
    # print(len(contentList))
    ###
    url = 'https://www.weather.go.kr/w/wnuri-sfct/today/short-term.do?topArea=12C20000&midArea=12C20100&btmArea=12C20100&unit=m%2Fs'
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.text
    else:
        print('웹 페이지에 접근할 수 없습니다.')

    soup = BeautifulSoup(page_content, 'html.parser')
    th = []
    my_list = []
    # thead 태그를 찾기
    thead = soup.find('thead').text
    thead = thead.replace('\n\n', '').replace('\n', ',')

    # 콤마(,)를 기준으로 문자열을 분리하여 리스트로 변환
    # 특정 문자열을 기준으로 문자열을 넣는다 .
    my_list = thead.split(",")
    print(my_list)
    # DivideSeaDict = {}
    tbodyList = []
    tbody = soup.find('tbody')
    tbody = tbody.find_all('td')
    # 27  0 9 18
    # 32
    my_dict = {}
    # 반복문을 사용하여 딕셔너리에 키-값 쌍 추가 (조건문 추가)
    print(len(tbody))
    trList = []
    if (len(tbody) == 27):  # tr이 3개인경우

        for i in range(0, len(tbody)):
            if i == 0 or i == 9 or i == 18:
                key = f'동해중부앞바다{i // 9}'  # 각각의 키를 고유하게 만듭니다.
                my_dict[key] = {
                    '날짜': tbody[i].get_text(strip=True),
                    '풍향': [tbody[i+1].get_text(strip=True), tbody[i+2].get_text(strip=True), tbody[i+5].get_text(strip=True), tbody[i+6].get_text(strip=True)],
                    '풍속': [tbody[i+3].get_text(strip=True), tbody[i+7].get_text(strip=True)],

                }
    print(my_dict)

    # if (len(tbody) == 32):  # tr이 3개인경우

    #     for i in range(0, len(tbody)):
    #         if i == 0 or i == 9 or i == 18:
    #             key = f'동해중부앞바다{i // 9}'  # 각각의 키를 고유하게 만듭니다.
    #             my_dict[key] = {
    #                 '날짜': tbody[i].get_text(strip=True),
    #                 '풍향': [tbody[i+1].get_text(strip=True), tbody[i+2].get_text(strip=True), tbody[i+5].get_text(strip=True), tbody[i+6].get_text(strip=True)],
    #                 '풍속': [tbody[i+3].get_text(strip=True), tbody[i+7].get_text(strip=True)],

    with open('./data/DivideSea.json', 'w', encoding='utf8') as data:
        json.dump(my_dict, data, indent=4, ensure_ascii=False)


except Exception as ex:
    print('Exception', ex)
''' 
# <a> 태그의 WebElement를 찾기

# <a> 태그의 href 속성 값을 가져오기
href = a_element.get_attribute("href")

# href 속성에 지정된 URL로 이동
driver.get(href)
'''
