import time
from selenium import webdriver  # 웹 브라우저 식별
from selenium.webdriver.common.by import By  # 웹 요소 식별
# 크롬 브라우저를 자동으로 설치해준다 .
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()  # webdriver option 설정
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # logging - 기록설정
driver = webdriver.Chrome(options=options)
