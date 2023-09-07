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


def ex2():
    fig.update_layout(
        title_y=0.9,
        title_x=0.5,
        title_xanchor='center',
        title_yanchor='middle',
        # 폰트 스타일 추가 부분
        title_font_size=25,
        title_font_color='red',
        title_font_family='Times'
    )
    fig.show()


def ex3():
    import plotly.express as px

    # 데이터 불러오기
    df = px.data.tips()

    fig = px.scatter(df, x='total_bill', y='tip')

    fig = px.scatter(df, x='total_bill', y='tip',
                     labels=dict(total_bill="Total Bill($)", tip="Tip ($)"))
    fig.show()
    # labels=dict(X 축 컬럼명="변경할 컬럼명", Y 축 컬럼명="변경할 컬럼명") 을 통해서 변경이 가능합니다.


def ex4():
    import plotly.express as px
    import plotly.graph_objects as go

    # 데이터 생성
    df = px.data.tips()
    x = df['total_bill']
    y = df['tip']
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

    fig.show()
    fig.update_xaxes(title_text='Total bill($)')
    fig.update_yaxes(title_text='Tip ($)')
    fig.show()

# 축 레이블은 글자크기 , 색  , 서체 변경이 가능


def ex5():
    fig.update_xaxes(title_font_size=30,
                     title_font_color='crimson',
                     title_font_family='Courier')
    fig.update_yaxes(title_font_size=30,
                     title_font_color='crimson',
                     title_font_family='Courier')
    fig.show()

# 축 타이틀 위치 지정 방법


def ex6():
    fig.update_xaxes(title_standoff=100)
    fig.update_yaxes(title_standoff=100)

    fig.show()


def ex7():
    import plotly.express as px

    # 데이터불러오기
    df = px.data.tips()

    # 그래프 그리기
    fig = px.scatter(df, x='total_bill', y='tip')

    #  축 레이블 삭제하기
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)

    fig.show()


# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
ex7()
