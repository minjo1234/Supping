# Keyword : Plotly 그래프 사이즈, Plotly graph size ,Plotly 그래프 마진, Plotly graph margin , Plotly width, Plotly height

# 1)express 그래프
import plotly.graph_objects as go
import plotly.express as px
fig = px.bar(x=['a', 'b', 'c'], y=[1, 3, 2], width=600, height=400)
fig.show()

# 2) graph_object 그래프
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2], ))
fig.update_layout(width=600, height=400)
# 축 타이틀 추가하기
fig.update_xaxes(title_text='number')
fig.update_yaxes(title_text='number result')

fig.show()


