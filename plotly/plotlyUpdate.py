import plotly.express as px

fig = px.bar(x=['a', 'b ', 'c '], y=[1, 2, 3], title='Title 설정하기 ')


def ex1():
    # 타이틀 위치 설정부분
    fig.update_layout(
        title_x=0.5,
        title_y=0.9,
        title_xanchor='center',
        title_yanchor='middle'

    )
    fig.show()


ex1()
