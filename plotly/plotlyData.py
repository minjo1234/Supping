# Plotly 제공 데이터셋
# plotly에서는 express 를 통해 데이터셋을 불러올수 있습니다.

# express 패키지 불러오기
import plotly.express as px

# 선거 데이터 불러오기
election = px.data.election()
election.head()
# head를 이용해서 위에서 5개 가져오기 .
print(election.head())


# 1. import plotly.express as px
# 2. px.data.가져오고싶은데이터()
# 3. 출력하고싶은 부분 가져오기 .
