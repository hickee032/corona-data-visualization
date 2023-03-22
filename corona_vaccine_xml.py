from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def vaccine_drow_chart():
    korean_font()
    plt.rcParams['font.size'] = 12
    plt.rcParams["figure.figsize"] = (15, 8)

    # 바 차트
    sido_x = ['서울', '부산', '대구', '인천', '광주', '대전', '경기']
    bar_width = 0.2
    data_1 = [829, 286, 200, 256, 125, 123, 1178]
    data_2 = [822, 283, 198, 253, 124, 122, 1167]
    data_3 = [114, 4, 24, 31, 16, 123, 148]
    # 그래프
    sido = ['서울', '부산', '대구', '인천', '광주', '대전', '경기']
    y1 = np.array([90, 87, 86, 89, 89, 87, 89])  # 1차 접종율
    y2 = np.array([89, 87, 85, 88, 88, 87, 88])  # 2차 접종
    y3 = np.array([13, 14, 11, 11, 12, 10, 12])  # 3차 접종

    bar_width = 0.4
    fig, ax1 = plt.subplots()
    ax1.plot(sido, y1, color='b', markersize=7, linewidth=3, alpha=0.7, label='1차 접종')
    ax1.plot(sido, y2, color='r', markersize=7, linewidth=3, alpha=0.7, label='2차 접종')
    ax1.plot(sido, y3, color='g', markersize=7, linewidth=3, alpha=0.7, label='3차 접종')

    ax1.set_xlabel('시도명')
    ax1.set_ylabel('접종률')
    bar_width = 0.2
    ax1.tick_params(axis='both', direction='in')
    ax2 = ax1.twinx()
    index = np.arange(len(sido_x))
    ax2.bar(index - bar_width, data_1, color='chartreuse', align='edge', width=bar_width, label='1차')
    ax2.bar(index, data_2, color='coral', align='edge', width=bar_width, label='2차')
    ax2.bar(index + bar_width, data_3, color='orange', align='edge', width=bar_width, label='3차')
    plt.xticks(index, sido_x)

    ax2.tick_params(axis='y', direction='in')
    plt.title('코로나 백신 접종 회차별 비교')
    ax1.set_zorder(ax2.get_zorder() + 10)
    ax1.patch.set_visible(False)
    # ax1.legend(loc='upper left')
    ax1.legend(loc='upper right')
    ax2.legend(loc='lower left')

    plt.show()