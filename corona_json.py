import json
import urllib.request
from urllib.parse import quote
import folium
from folium import plugins
import pandas as pd
import _excel as excel

# csv data 읽어오rl -> dict
def csv_data_read():
    df = pd.read_csv('data_file\covid19.csv', encoding='cp949')
    print(df)
    df.head()
    cojs_dict = df.to_dict()
    return cojs_dict,df

# 엑셀 파일로 쓰기
def toexceljson(cojs_dict):
    excel.excel_writer('excel\corona_json_excel', cojs_dict)


def drow_map_chart(df):
    # 맵 데이터(지도)를 읽어오기
    geo_data = json.load(open('map_data\kor_map.json', encoding='utf-8'))
    center = [36.878534, 127.823793]
    # 맵을 두개 띄우기
    m = folium.plugins.DualMap(location=center, zoom_start=8)
    plugins.Fullscreen(position='topright',
                       title='Click to Expand',
                       title_cancel='Click ti Exit',
                       force_separate_button=True).add_to(m)
    plugins.MousePosition().add_to(m)
    # 맵 지도 데이터와 csv데이터를 매핑함
    choropleth1 = folium.Choropleth(
        geo_data=geo_data,
        data=df,
        columns=('gubun', 'defCnt'),
        key_on='feature.properties.CTP_KOR_NM',
        fill_color='RdYlGn',
        legend_name='누적 확진자수'
    ).add_to(m.m1)

    choropleth2 = folium.Choropleth(
        geo_data=geo_data,
        data=df,
        columns=('gubun', 'defCnt'),
        key_on='feature.properties.CTP_KOR_NM',
        fill_color='OrRd',
        legend_name='해외유입 확진자수 '
    ).add_to(m.m2)
    # 라벨 설정
    choropleth1.geojson.add_child(folium.features.GeoJsonTooltip(['CTP_KOR_NM'], labels=False))
    choropleth2.geojson.add_child(folium.features.GeoJsonTooltip(['CTP_KOR_NM'], labels=False))

    title_html = '<h3 align="center" style="font-size:20px"><b>확진자 지도</b></h3>'
    m.get_root().html.add_child(folium.Element(title_html))
    folium.LayerControl().add_to(m)

    # 듀얼 맵은 창으로 띄울수 없다
    try:
        print('html 파일 저장')
        m.save('html\confirm_map.html')
    except Exception as ex:
        print('html 파일 저장 오류')
