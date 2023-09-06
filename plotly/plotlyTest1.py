# graph_objects 패키지를  go 로 불러옴
import plotly.express as px
import plotly.graph_objects as go

# go.Figure() 함수를 활용하여 기본 그래프를 생성
fig = go.Figure(
    # Data 입력
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    # layout 입력
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)
# show하면 내 노트북 (주피터 노트북 등)에 그래프가 나타남.
fig.show()

# express 패키지를  px로 불러옴


# import plotly.graph_objects as go
# import plotly.express as px
# 막대그래프를 제작하는 것으로  plotly.graph_objects as go를 이요하여 작성할 수 있고
# go.Figure로 기본그래프 생성 go.Figure(data,layout)
# go.Figure에는 매개인자를 두 개받을 수 있는데 보통 data 와 layout이 존재한다  .
# go.Figure data -> data Type이 무수히 올 수 있으며
# go.Figure layout에는 -> title, axes, shape , margins 가 존재한다 .
# 3) Figure 랜더링
# fig.show()
# Figure를 받은 객체에 show() 함수를 마지막에 작성하면 랜더링 과정을 통해 내 주피터 노트북 출력 셀에 그래프가 나타납니다.

fig = px.bar(x=['a', 'b', 'c'], y=[1, 3, 2],
             title='A figure specified by express')
fig.show()


# bar -> 막대 그래프
# 세세한 그래프를 요구할경우 graph_objects 를 사용하고
# 간결한 그래프를 보고싶을 경우 코드가 적은 express를 사용한다 .
