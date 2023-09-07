import pandas as pd
import time
import datetime
import plotly.express as px
import plotly.graph_objects as go

# 18tour.py
import json
import urllib.request


def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            rcv = response.read()

        return rcv
    except Exception as ex:
        print('에러', ex)
        return '수요일 졸임의 예외처리'

    # Request -> HTTP 요청의 설정과 관련된 객체이며 ,
    # urlopen은 실제로 실행하며 서버와 통신하고 데이터를 가져옵니다 .'


def getNatVistor(yyyymm, nat_cd, ed_cd):
    # http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?serviceKey + &YM=201201&NAT_CD=112&ED_CD=E'
    serviceKey = 'F0kz%2BWp8tztnB9CWRGwdy5924Ujgtp%2Bt%2FMw2%2FmirhMzzSFR8QAtnG2eqG1ZgUK6qfkrM4YUJ18qNfMAlcG%2BkDw%3D%3D'
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameter = '?_type=json&serviceKey='+serviceKey
    parameter = parameter + '&YM=' + yyyymm
    parameter = parameter + '&NAT_CD=' + nat_cd
    parameter = parameter + '&ED_CD=' + ed_cd
    url = url + parameter

    print(url)

    ret = get_request_url(url)  # 9라인 함수호출
    print('결과값', ret)
    if ret == None:
        None
    else:
        return json.loads(ret)  # 변경될예정 #json데이터 json.loads(ret)


result = []
for year in range(2019, 2021):
    for month in range(1, 3):
        yyyymm = '{0}{1:0>2}'.format(str(year), str(month))
        json_data = getNatVistor(yyyymm, '275', 'E')  # 275미국국가코드 e 방한외국인
        if (json_data['response']['header']['resultMsg'] == 'OK'):
            # 태그명을 입력해서 차례대로 들어간다 .
            natKorNm = json_data['response']['body']['items']['item']['natKorNm']
            num = json_data['response']['body']['items']['item']['num']
            print('%s %s %s' % (str(year), str(month), 'kim'))
            result.append([yyyymm]+[natKorNm]+['275']+[num])

time.sleep(1)
print()
print(result)
print()
'''
웹에서 데이터 크롤링
    ㄴ 첫번째 
'''
