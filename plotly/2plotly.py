import plotly.express as px
# 데이터 불러오기
import plotly.graph_objects as go


def ex1():

    # 데이터 불러오기
    df = px.data.tips()

    # 그래프 그리기
    fig = px.scatter(df, x='total_bill', y='tip')
    fig.show()


def ex2():
    df = px.data.tips()
    x = df['total_bill']
    y = df['tip']
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

    fig.update_xaxes(title_text='Total Bill ($)')
    fig.update_yaxes(title_tex='Tip ($)')


ex1()
