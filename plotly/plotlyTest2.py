
# Plotly에서 그래프를 그리는 가장 보편적인 방법은 아래 그림과 같이 기초 그래프를 생성 후 다양한 방법으로 그래프를 업데이트하는 2단계를 거치는 방법입니다. 이번 장에서는 2번째 단계인 그래프를 업데이트 하는 5가지의 함수 기능에 대해 간략히 설명드리겠습니다.
# 그래프를 graph_objects 로 생성하거나 express 를 이용해서 5가지 업데이트를 통한다 .

import plotly.express as px
import plotly.graph_objects as go

# add_trace 요소를 더해준다 .

# fig = go.Figure()
# fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
# fig.show()


# 데이터 불러오기
df = px.data.iris()

fig = px.scatter(df, x='sepal_width', y='sep_length', color='species',
                 title='using the add trace() method with a plotly express figure')

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode='lines',
        line=go.scatter.Line(color='gray'),
        showlegend=False)
)

fig.show()

# bar 막대 그래프
# scatter 선점도
# scatter.Line 줄을 추가하겠다 .
# mode='lines': Scatter 그래프를 선 그래프로 표시합니다.
# showlegend=False: 범례에 표시하지 않음을 설정합니다.
# 범례(Legend)는 서로다른 종류의 데이터를 색깔 또는 마커 모양으로 분류하고 표시하는 기능합니다.


# 1. add_trace
# 2. update_trace
