import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import copy
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import _excel as excel


def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False  # 차트 시각화 할때 ( - ) 부호 처리


# 날짜 처리 월 약어 -> 숫자로 -> 타입 str
def get_month(key):
    month = ''
    month_num = {'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4', 'May': '5', 'Jun': '6',
                 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12',
                 }.get(key)
    month = month_num
    return month


# 날짜 처리 년도 붙여주기 -> 타입 str -> 리턴 리스트
def year_month(start_year, date_temp):
    # print(date_temp)
    year = start_year  # 2020
    date_list_r = []
    for dr in range(len(date_temp) - 1, -1, -1):
        date_t = str(year) + '.' + date_temp[dr]
        # print(date_t)
        date_list_r.append(date_t)
        if date_temp[dr] == '12.31':
            year += 1
    return date_list_r


def url_set_soup():
    # 속도 느림
    # URL = 'https://covid.observer/kr/'
    # page = urlopen(URL)
    # doc = page.read()
    # page.close()
    # soup = BeautifulSoup(doc, 'html5lib')
    # print(soup)

    URL = 'https://covid.observer/kr/'
    res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def datelist_set(soup):
    # 날짜 정보 -> 리스트
    date_list = []
    date_result = []
    date_all = soup.find_all('td', class_='date')
    # 1102 # 1
    for i in date_all:
        date_list.append(get_month(i.text[0:3]) + '.' + i.text[4:])
    date_result = year_month(2020, date_list)
    print(date_result)
    return date_result


# 누적 확진자 정보
def confirmlist_set(soup):
    confirm_list = []
    confirm = soup.select('tbody > tr')
    for cf in confirm:
        confirm_list.append(float(cf.select('td:nth-of-type(6)')[0].get_text().strip().replace(',', '')) / 1000)
    confirm_list.reverse()
    return confirm_list


# 증가치
def increaselist_set(soup):
    increase_list = []
    confirm_increase = soup.select('tbody > tr')
    for inf in confirm_increase:
        increase_list.append(int(inf.select('td:nth-of-type(5)')[0].get_text().strip().replace(',', '')))
    increase_list.reverse()
    return increase_list


# 일차 리스트
def countlist_set(date_result):
    count_list = list(range(len(date_result)))
    return count_list


# 일차, 누적 확진자 -> dict
def listdict_set(count_list, confirm_list, increase_list):
    dic_temp = dict(zip(count_list, confirm_list))
    df = pd.DataFrame({'일차': dic_temp.keys(),
                       '누적확진자': dic_temp.values()})

    dic_temp2 = dict(zip(count_list, increase_list))
    df2 = pd.DataFrame({'일차': dic_temp2.keys(),
                        '증가세': dic_temp2.values()})
    return dic_temp, dic_temp2


def confirmchart_drow(dic_temp, dic_temp2):
    # 설정
    # 한글 설정
    plt.rc('font', family='NanumBarunGothic')
    # 캔버스 사이즈 적용
    plt.rcParams["figure.figsize"] = (18, 18)

    # 차트 설정
    # # x축 폰트 사이즈
    # # plt.xticks(fontsize=0)
    # # x축 안보이게 설정
    # plt.gca().axes.xaxis.set_visible(False)
    # # 범례 설정 -> 리스트
    # leg_list = ['x1000']
    # plt.legend(leg_list)
    #
    # sns.barplot(data=df, x='일차', y='누적확진자', color='yellow')
    # plt.title('누적확진자 증가량')
    # plt.show()

    fig, ax1 = plt.subplots()
    ax1.bar(dic_temp.keys(), dic_temp.values(), color='orange')
    ax1.set_xlabel('일차')
    ax1.set_ylabel('누적 x1000')

    ax2 = ax1.twinx()
    ax2.plot(dic_temp.keys(), dic_temp2.values(), color='green')
    ax2.set_ylabel('증가량')

    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)

    plt.title('누적확진자 증가량')
    plt.show()

def toexcelhtml(dict_excel):
    print('엑셀로 저장됩니다.')
    excel.excel_writer('excel\corona_html_excel', dict_excel)