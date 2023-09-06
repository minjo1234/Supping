import matplotlib.pyplot as plt
import pandas as pd
import time
import seaborn as sns
from matplotlib import rc

rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False
fname = './data/navercm.csv'
df = pd.read_csv(fname, encoding='utf8')
print(df)
ax = df.plot(kind='bar', x='nick', y='recomm',
             figsize=(15, 8), legend=True, fontsize=12)
ax.set_xlabel('닉네임', fontsize=12)
ax.set_ylabel('조회수임', fontsize=12)
ax.legend(['닉네임', '조회수'], fontsize=12)
plt.show()

time.sleep(1)
fname = './data/navercm.csv'
df = pd.read_csv(fname, encoding='utf8')
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='nick', y='recomm')
plt.show()

# figsize는 가로크기와 세로크기를 가르킨다 .

# 인터파크 , 네이버웹툰 ,공공데이터
