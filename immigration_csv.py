import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import sys
import cx_Oracle


# 한글 폰트
def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_csv('data_file/immigration_year.csv', sep=',', encoding='cp949')

# 출국자 국민 외국인으로 구분
def departure_data():
    df = pd.read_csv('data_file/immigration_year.csv', sep=',', encoding='cp949')
    departure_all = df[(df['출입국구분'] == '출국')]
    departure = df[(df['출입국구분'] == '출국') & (df['국민외국인여부'] == '국민')]
    departure_for = df[(df['출입국구분'] == '출국') & (df['국민외국인여부'] == '외국인')]
    print('\033[96m' + '-----출국 내국인-----')
    print(departure)
    print('\033[93m' + '-----출국 외국인-----')
    print(departure_for)

    print('' + '\033[0m')
    return departure, departure_for


# 입국자 국민 외국인으로 구분
def Entrance_data():
    df = pd.read_csv('data_file/immigration_year.csv', sep=',', encoding='cp949')
    entry_all = df[(df['출입국구분'] == '입국')]
    entry = df[(df['출입국구분'] == '입국') & (df['국민외국인여부'] == '국민')]
    entry_for = df[(df['출입국구분'] == '입국') & (df['국민외국인여부'] == '외국인')]
    print('\033[96m' '-----입국 내국인-----')
    print(entry)
    print('\033[93m' + '-----입국 외국인-----')
    print(entry_for)
    print('' + '\033[0m')
    return entry, entry_for


# 엑셀로 저장하기
def excel_writer(departureAll, entryAll):
    # 출국자
    departureAll.to_excel("excel\immigration_year_departure.xlsx")
    # 입국자
    entryAll.to_excel("excel\immigration_year_entry.xlsx")


'''
# 엑셀파일 읽기
departure_all = pd.read_excel("excel\immigration_year_departure.xlsx")
entry_all = pd.read_excel("excel\immigration_year_entry.xlsx")
'''

def dep_ent_drow_chart(departure, departure_for,entry, entry_for):
    # 그래프로 표시
    korean_font()
    plt.rcParams["figure.figsize"] = (15, 8)

    # 국민 출국 그래프
    x1 = departure['년']
    y1 = departure['출입국자수']
    plt.subplot(1, 2, 1)
    plt.plot(x1, y1, color='orange', marker='o', linestyle='solid')
    plt.title('2011~2021 년도별 출국자')
    # 외국인 출국 그래프
    plot = plt.plot(departure_for['년'], departure_for['출입국자수'], color='blue', marker='o', linestyle='solid')
    plt.legend(['내국인', '외국인'], fontsize=12)  # 범례 지정
    plt.title('년도별 출국자')
    plt.xlabel('년도', fontsize=10)
    plt.ylabel('인원 수', fontsize=10)
    plt.grid(True)

    # 국민 입국 그래프
    plt.subplot(1, 2, 2)
    x2 = entry['년']
    y2 = entry['출입국자수']
    plt.plot(x2, y2, color='orange', marker='o', linestyle='solid')
    plt.title('2011~2021 년도별 입국자')
    # 외국인 입국 그래프
    plot = plt.plot(entry_for['년'], entry_for['출입국자수'], color='blue', marker='o', linestyle='solid')
    plt.legend(['내국인', '외국인'], fontsize=12)  # 범례 지정
    plt.title('년도별 입국자')
    plt.xlabel('년도', fontsize=10)
    plt.ylabel('인원 수', fontsize=10)
    plt.grid(True)

    plt.show()
