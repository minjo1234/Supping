import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from matplotlib import rc
from sklearn.linear_model import LinearRegression

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.
# 빈 배열 가져오기
data = []
# 연도별 경기 수 데이터
years = range(2014, 2024)  # 2014년부터 2023년까지
# 경기수 MatchNum
MatchNum = []

# csv 파일 읽어와서 경기 수 구하기
for i in range(10):
    with open(f'./betmandata/betman{2014+i}.csv', newline='', encoding='utf-8') as csvfile:
        data = []
        reader = csv.reader(csvfile)

        for row in reader:
            data.append(row)

        MatchNum.append(len(data))

# 경기수
print(MatchNum)

# 그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(years, MatchNum, marker='o', linestyle='-')
plt.title('연도별 경기 수')
plt.xlabel('연도')
plt.ylabel('경기 수')
plt.grid(True)


# 그래프 표시
# 선형 회귀 모델을 훈련하기 위해 데이터를 준비합니다.
X = np.array(years).reshape(-1, 1)  # 연도를 특성으로 사용
y = np.array(MatchNum)  # 경기 수를 타겟으로 사용

# 선형 회귀 모델 생성 및 훈련
model = LinearRegression()
model.fit(X, y)

# 예상 그래프 생성
predicted_y = model.predict(X)

# 예상 그래프 추가
plt.plot(years, predicted_y, marker='x', linestyle='--', label='예상 경기 수')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()

# def WinAndLose(data):
#     for i in range(len(data)):
#         if data[i]

#
