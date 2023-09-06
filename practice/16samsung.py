# import
from matplotlib.ticker import FuncFormatter
import pandas as pd
import datetime
import schedule  # pip install schedule
from bs4 import BeautifulSoup as BeautifulSoup  # pip install bs4
import time
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
import re
import plotly.express as px
import xlwt
# webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# matplotlib 한글 is available
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


x_val = []
y_val = []
count = 0
total = 0

# driver.get()
url = 'https://finance.daum.net/quotes/A005930#home'
driver.get(url)

pathxls = './data/samsung.xlsx'
# 주식체크 check()

# def check()


def check():
    global x_val
    global y_val
    global count
    global total
    global pathxls
    # html parsing and parsing data print
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    test1 = soup.select(
        '#boxSummary > div > span:nth-child(1) > span.currentB > span.numB.down > strong')  # 삼성전자주식값 70,700
    msg = str(test1)
    # print('주식 가격 = ', msg)

    # 숫자추출 and 3번째마다 , 추가
    numbers = re.sub(r'[^0-9]', '', msg)
    numbers = numbers[0:2] + ',' + numbers[2:]

    # 추가
    total += 1

    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')

    # print()
    # print('-'*50)
    # print('현재시간 삼성전자 주가', nowTime, '------>', numbers)
    y_val.append(numbers)
    x_val.append(nowTime)


# 주석 1회호출 check()
schedule.every(0.1).seconds.do(check)

for i in range(10):
    # print('ㄴ i=', i)
    # print('주식금액', y_val)
    # print('거래시간', x_val)
    # 스케줄 실행
    schedule.run_pending()
    count += 1

    time.sleep(1)
    if count > 9:
        stock = {
            'time': x_val,
            'price': y_val
        }
        pathxls = './data/samsung.xlsx'
        df = pd.DataFrame(stock)
        df.to_excel(pathxls)
        schedule.cancel_job(check)
        break

# 선 그래프 생성
plt.figure(figsize=(12, 6))  # 가로세로를 지정하다
plt.plot(x_val, [int(price.replace(',', '')) for price in y_val])

# Y축 레이블 서식화 함수 정의


def y_format(x, _):
    return f'{x:,.0f}'  # 80,000 형식으로 포맷 -> 0,000에는 ,를사용하고 0f까지 출력한다 .

# Y축에 서식을 적용
# plt.gca().yaxis.set_major_formatter(FuncFormatter(y_format))
# plt.title('삼성전자 주식 가격 변화')
# plt.xlabel('시간')
# plt.ylabel('주식 가격')
# plt.xticks(rotation=45)  # x 축 레이블을 더 잘 볼 수 있게 회전
# # y축의 최소값과 최대값 설정 (예: 최소값 70,000, 최대값 80,000으로 설정)
# # 그래프 표시
# plt.tight_layout()
# plt.show()


df = pd.DataFrame(
    {'시간': x_val, '주식 가격': [int(price.replace(',', '')) for price in y_val]})
fig = px.line(df, x='시간', y='주식 가격', title='삼성전자 주식 가격변화 ')
fig.show()

driver.close()


# x_val과 y_val을 데이터프레임으로 만듭니다.
# df = pd.DataFrame(
# {'시간': x_val, '주식 가격': [int(price.replace(',', '')) for price in y_val]})
# # df pd.DataFrame ( 변수를 넣어준다 )
# # Plotly를 사용하여 그래프 생성
# fig = px.line(df, x='시간', y='주식 가격', title='삼성전자 주식 가격 변화')
# fig.update_xaxes(type='category')  # X축을 범주형으로 설정하여 시간을 연속적으로 표시하지 않도록 합니다.

# 그래프 표시
# fig.show()
