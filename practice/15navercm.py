from matplotlib import rc
import pandas as pd
import csv as csv
import seaborn as sns
import matplotlib.pyplot as plt
fname = './data/navercm.csv'
df = pd.read_csv(fname, encoding='utf-8')
print(df)
rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.
# 문제 1 bar모양클래스 df.plot(kind='bar')
# 문제2 sns.barplot
# 문제 2 bar모양클래스 df.plot(kind='bar')
# pie, line , scatter ,hist
# 막대 그래프 생성

df.plot(kind='bar')
plt.show()

# 막대 그래프 생성
sns.barplot(data=df)
plt.show()

df['recomm'].value_counts().plot(kind='pie', autopct='%1.1f%%')

# 원형 차트에 레이블 및 제목을 추가하려면 필요한 경우 다음과 같이 합니다.
plt.xlabel('추천 값')
plt.ylabel('개수')
plt.title('추천 값의 원형 차트')

# 차트를 표시합니다.
plt.show()
