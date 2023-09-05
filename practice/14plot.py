# 10graphpie.py
import time
import matplotlib.pyplot as plt
import seaborn as sns  # dataset ( pip install seaborn )
from matplotlib import font_manager
from matplotlib import rc
import numpy as np
import seaborn as seaborn
import matplotlib as mpl
import pandas as pd
import time

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.
'''
# 점 그래프로 나타낸다
name = ['푸바오', '동바오', '길동', '연희']
data = [40, 50, 86, 35]
ep = [0.05, 0.1, 0.15, 0.05]  # 슬라이싱되는 값
# explode 슬라이싱, shadow=True그림자효과 시작각도 starangle
fig = plt.figure()
fig, plt.pie(data, explode=ep, labels=name,
             autopct='%0.1f%%', shadow=True, startangle=90)
plt.show()
'''
# Finalize the plot

print()
penguins = sns.load_dataset('penguins')
print(penguins.head())
print()
print(penguins.columns)
print()
print(penguins.info())

# 파이썬의 대표적인 시각화도구로 matplotlib 과 seaborn 이 존재한다 .

print()
tips = sns.load_dataset('tips')
print()
print(tips.head())
print()
print(tips.columns)
print()

ax = plt.subplot(111)
ax = sns.barplot(x='tip', y='day', data=tips, capsize=0.2)
ax.set_title('sns day tip graph')
ax.set_xlabel('tip money')
ax.set_ylabel('day')
plt.show()

print()
titanic = sns.load_dataset('titanic')
print(titanic.head())
print()
print(titanic.columns)
print()
print(titanic.info())

sns.countplot(x='class', data=titanic)
plt.title('타이타닉호 각 클래스별 승객의 수 ')
plt.show()


# 빅데이터 시에 기본적으로 이용하는 것이 비행기 , 아이리스 , 타이타닉등이 존재한다 .
# 방금전의 도표로는 신뢰성이 조금 낮다 .

print()
print()
print()

print()

fruits = ['apple', 'banana', 'cherry', 'grape']
area = ['제주', '부산', '대구', '광주']
su1 = [100, 200, 300, 40]
su2 = [100, 200, 300, 400]
su3 = [100, 200, 300, 400]
su4 = [77, 21, 65, 45]
df = pd.DataFrame({area[0]: su1, area[1]: su2, area[2]
                  : su3, area[3]: su4}, index=fruits)
print(df)
print()
print(df['제주'])
print()
# print(df.loc[1:3])
print(df.info())

# pands와 Maplotli을 이용해서 도표를 만들었다 .
time.sleep(1)
ax = df.plot(kind='bar', figsize=(10, 5))
plt.legend(loc='upper right')
plt.show()
