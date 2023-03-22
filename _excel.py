# Excel 관련
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame


# 확장자 .xlsx

# 부호 한글 처리
def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


# Dictionary -> Excel 파일로 쓰기 (.xlsx)
def excel_writer(file_name, dic):
    file_name += '.xlsx'
    korean_font()
    df = DataFrame.from_dict(dic)
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1',index=[0])
    writer.close()  # 닫아줘야한다
