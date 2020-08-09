# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:51:22 2020

@author: Jeongheum Lee
"""
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
url='https://pythondojang.bitbucket.io/weather/observation/currentweather.html'
response = requests.get(url)
#response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
soup = BeautifulSoup(response.content, 'html.parser')
 
table = soup.find('table', { 'class': 'table_develop3' })    # <table class="table_develop3">을 찾음
data = []                            # 데이터를 저장할 리스트 생성
for tr in table.find_all('tr'):      # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
    tds = list(tr.find_all('td'))    # 모든 <td> 태그를 찾아서 리스트로 만듦
                                     # (각 날씨 값을 리스트로 만듦)
   # print(tds)
    for td in tds:                   # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
        if td.find('a'):             # <td> 안에 <a> 태그가 있으면(지점인지 확인)
            point = td.find('a').text    # <a> 태그 안에서 지점을 가져옴
          #  print(point)
            weather_condition = tds[1].text    # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            temperature = tds[5].text    # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
            figure_comport=tds[7].text   # 2020.8.9 불쾌지수(인덱수 7) 추가 
          #  print(temperature)
            humidity = tds[9].text       # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
            wind_velocity=tds[11].text    # 2020.8.9 풍속(m/s) (인덱수11) 추가 
         #   print(humidity)
 #           data.append([point, temperature, humidity])    # data 리스트에 지점, 기온, 습도를 추가
            data.append([point, temperature, figure_comport, humidity, wind_velocity])    # data 리스트에 지점, 기온, 습도를 추가

 
data    # data 표시. 주피터 노트북에서는 print를 사용하지 않아도 변수의 값이 표시됨

with open('weather.csv', 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
#with open('weather.xlsx', 'w') as file:    # weather.csv 파일을 쓰기 모드로 열기
    #file.write('point,temperature,humidity\n')                  # 컬럼 이름 추가
    file.write('point, temperature, figure_comport, humidity, wind_velocity\n')
    #file.write('지점, 온도, 불쾌지수, 습도, 풍속 \n')
    for i in data:                                              # data를 반복하면서
        # file.write('{0},{1},{2}\n'.format(i[0], i[1], i[2]))    # 지점,온도,습도를 줄 단위로 저장
        file.write('{0},{1},{2},{3},{4}\n'.format(i[0], i[1], i[2], i[3], i[4]))    # 지점,온도,습도를 줄 단위로 저장
        
#data.to_excel('weather.csv')        


# %matplotlib inline을 설정하면 matplotlib.pyplot의 show 함수를 호출하지 않아도
# 주피터 노트북 안에서 그래프가 표시됨
#%matplotlib inline
import pandas as pd                # 데이터를 저장하고 처리하는 패키지
import matplotlib as mpl           # 그래프를 그리는 패키지
import matplotlib.pyplot as plt    # 그래프를 그리는 패키지
 
# csv 파일을 읽어서 DataFrame 객체로 만듦. 인덱스 컬럼은 point로 설정, 인코딩은 euc-kr로 설정
df = pd.read_csv('weather.csv', index_col='point', encoding='euc-kr')
#df = pd.read_excel('weather.xlsx')
#df = pd.read_csv('weather.csv', encoding='euc-kr')
df    # df 표시

# 특별시, 광역시만 모아서 DataFrame 객체로 만듦
# city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산','울산', '수원']]
# city_df    # city_df 표시

# # Windows 한글 폰트 설정
# font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
# mpl.rc('font', family=font_name)
 
# #차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
# ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
# ax.set_xlabel('도시', fontsize=12)          # x축 정보 표시
# ax.set_ylabel('기온/습도', fontsize=12)     # y축 정보 표시
# ax.legend(['기온', '습도'], fontsize=12)    # 범례 지정
# plt.show()
