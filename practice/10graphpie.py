# 10graphpie.py
import matplotlib.pyplot as plt

from matplotlib import font_manager
from matplotlib import rc
import numpy as np

import matplotlib as mpl


rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # 추가해줍니다.

# 점 그래프로 나타낸다
name = ['푸바오', '동바오', '길동', '연희']
data = [40, 50, 86, 35]
ep = [0.05, 0.1, 0.15, 0.05]  # 슬라이싱되는 값
# explode 슬라이싱, shadow=True그림자효과 시작각도 starangle
fig = plt.figure()
fig, plt.pie(data, explode=ep, labels=name,
             autopct='%0.1f%%', shadow=True, startangle=90)
plt.show()
