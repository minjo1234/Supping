import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.weather.go.kr/w/ocean/forecast/daily-forecast.do')
    # /html/body/div[2]/section/div/div[2]/div[2]/div/div[2]/a
    # 버튼 웹 요소 찾기
    a_element = driver.find_element(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div[2]/div/div[2]/a')
    href1 = a_element.get_attribute("href")
    driver.get(href1)
    driver.implicitly_wait(5)

    b_element = driver.find_element(
        By.XPATH, '//*[@id="rdo_sea_config_top6"]')
    href2 = b_element.get_attribute("href")
    driver.get(href2)
    driver.implicitly_wait(5)

    c_element = driver.find_element(
        By.XPATH, '//*[@id="rdo_sea_config_mid0"]')
    href3 = a_element.get_attribute("href")
    driver.get(href3)
    driver.implicitly_wait(5)

    d_element = driver.find_element(
        By.XPATH, '//*[@id="rdo_sea_config_btm0"]')
    href4 = a_element.get_attribute("href")
    driver.get(href4)
    driver.implicitly_wait(5)
    # 날짜선택

    # 날짜보기
    button6_element = driver.find_element(
        By.XPATH, '//*[@id="sub-sea-config"]/div[2]/ul/li/button')

    # button6 클릭 - JavaScript를 사용한 클릭
    driver.execute_script("arguments[0].click();", button6_element)
    driver.implicitly_wait(5)

    h3 = []
    title = driver.find_element(
        By.XPATH, '/html/body/div[2]/section/div/div[2]/div[4]/div')
    print(type(title))
    # /html/body/div[2]/section/div/div[2]/div[4]/div
    h3 = title.find_element(By.TAG_NAME, 'h3')
    print(h3.text)

    time.sleep(5)

except Exception as ex:
    print('Exception', ex)
'''
# <a> 태그의 WebElement를 찾기

# <a> 태그의 href 속성 값을 가져오기
href = a_element.get_attribute("href")

# href 속성에 지정된 URL로 이동
driver.get(href)
'''
