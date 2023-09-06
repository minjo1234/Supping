import schedule
from bs4 import BeautifulSoup as BeautifulSoup
from selenium import webdriver


options = webdriver.ChromeOptions()  # webdriver option 설정
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # logging - 기록설정
driver = webdriver.Chrome(options=options)


url = 'https://finance.daum.net/quotes/A005930#home'
driver.get(url)
