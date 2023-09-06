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
        return '수요일 졸려요'
    except Exception as ex:
        print('에러', ex)
        return '수요일 졸임의 예외처리'


def getNatVistor(yyyymm, nat_cd, ed_cd):
    # http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?serviceKey + &YM=201201&NAT_CD=112&ED_CD=E'
    serviceKey = '6kNS80LAr70h8NBAdKUk5ZS03ku6ZwZ%2Fc2UObO8MBqdvBdj5Rkvbc7Pjz6%2BPDntVgb0v30Dv8r2XDtDGl3tW7A%3D%3D'
    url = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList?serviceKey=6kNS80LAr70h8NBAdKUk5ZS03ku6ZwZ%2Fc2UObO8MBqdvBdj5Rkvbc7Pjz6%2BPDntVgb0v30Dv8r2XDtDGl3tW7A%3D%3D&YM=201201&NAT_CD=112&ED_CD=E'
    parameter = '?_type=json&service='+serviceKey
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
        return ret  # 변경될예정 #json데이터 json.loads(ret)


result = []
for year in range(2019, 2021):
    for month in range(1, 3):
        yyyymm = '202105'
        json_data = ''
        getNatVistor(yyyymm, '275', 'E') #275미국코드 , D=국민해외관광객  E=방한외래관광객 
        

'''
웹에서 데이터 크롤링
    ㄴ 첫번째 
'''
