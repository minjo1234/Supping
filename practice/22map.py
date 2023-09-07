import folium
import webbrowser
import os
import time

# map 설정
m = folium.Map(location=[37.5671, 126.9774], zoom_start=14)
# 마커 넣기
folium.Marker([37.5671, 126.9774], tooltip='seoul시청',
              icon=folium.Icon(icon='book')).add_to(m)

# 저장하고 출력
m.save('./data/index.html')
# 실제 경로나 realpath중 하나를 사용해야한다.4ㅌ₩
webbrowser.open('file://'+os.path.realpath('./data/index.html'))

print('서울 덕수궁 지도 표시')
