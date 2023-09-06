import plotly.graph_objects as go
import plotly.express as px

# 1)Title
fig = px.bar(x=['a', 'b', 'c'], y=[1, 3, 2], title='Title 설정하기')
fig.show()

# 2)graph_objects 그래프


# go Figure , data = go.type , layout = go.Layout설정
fig = go.Figure(
    data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]),
    layout=go.Layout(title=go.layout.Title(text='Title 설정하기'))
)

fig.show()
# 3)update_layout
fig = px.bar(x=['a', 'b', 'c'], y=[1, 3, 2])

fig.update_layout(title_text='타이틀 입력')
fig.show()

# 4) fig.update_layout
# fig.update_layout(
#             title_x = (0~1) 사이값
#             title_y = (0~1) 사이값
#             title_xanchor = (`auto","left","center","right")
#             title_yanchor = ("auto","top","middle","bottom")
#             })

fig = px.bar(x=['a', 'b', 'c'], y=[1, 2, 3], title='Title설정하기')

# 타이틀 위치 설정부분
fig.update_layout(
    title_x=0.5,
    title_y=0.9,
    title_xanchor='center',
    title_yanchor='middle'
)

fig.show()
