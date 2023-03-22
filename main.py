from bs4 import BeautifulSoup
import _excel as excel
import corona_html as ch
import corona_json as cj
import corona_vaccine_xml as cvx
import immigration_csv as imc

dict_excel = {}
cojs_dict = {}

departure = {}
departure_for = {}
entry = {}
entry_for = {}

err_prevention = 0


def menu():
    print('메뉴 선택  0 번은 종료')
    print('1. 확진자 차트 보기')
    print('2. 확진자 지도 시각화 보기')
    print('3. 확진자 데이터 엑셀 출력')
    print('4. 2011~2021 출입국자 데이터 보기')
    print('5. 2011~2021 출입국자 차트 보기')
    print('6. 누적 백신 접종자 그래프 보기')
    print('메뉴 선택')
    print('메뉴 선택')
    select_num = int(input('번호를 선택 : '))
    print(select_num)
    return select_num


def select(num):
    global dict_excel
    global cojs_dict
    global err_prevention

    global departure
    global departure_for

    global entry
    global entry_for

    select_no = num

    if select_no == 1:
        print('확진자 그래프 보기')
        soup = ch.url_set_soup()
        # 날짜 정보
        date_list = ch.datelist_set(soup)
        # 누적 확진자 정보
        confirm_list = ch.confirmlist_set(soup)
        # 증가치
        increase_list = ch.increaselist_set(soup)
        # 일차
        day_count_list = ch.countlist_set(date_list)
        # 리스트 -> 딕셔너리
        dict_confirm, dict_increase = ch.listdict_set(day_count_list, confirm_list, increase_list)
        ch.confirmchart_drow(dict_confirm, dict_increase)
        # 엑셀로 저장
        dict_excel = dict(zip(date_list, zip(increase_list, confirm_list)))
        # dict_excel = dict_confirm
        print(dict_excel)
        err_prevention = 1
        print(err_prevention)

    elif select_no == 2:
        if err_prevention == 1:
            cojs_dict, df = cj.csv_data_read()
            cj.drow_map_chart(df)
            cj.toexceljson(cojs_dict)
            err_prevention = 2
        else:
            print('정보확인이 필요합니다. 1번 -> 2번 -> 3번 차례로 접근하세요')

    elif select_no == 3:
        print(err_prevention)

        if err_prevention == 2:
            ch.toexcelhtml([dict_excel])
            cj.toexceljson(cojs_dict)
            err_prevention = 3
        else:
            print('정보확인이 필요합니다. 1번 -> 2번 -> 3번 차례로 접근하세요')

    elif select_no == 4:
        if err_prevention == 3:
            departure, departure_for = imc.departure_data()
            entry, entry_for = imc.Entrance_data()
        else:
            print('정보확인이 필요합니다. 1번 -> 2번 -> 3번 차례로 접근하세요')

    elif select_no == 5:
        if err_prevention == 4:
            imc.dep_ent_drow_chart(departure, departure_for, entry, entry_for)
        else:
            print('정보확인이 필요합니다. 1번 -> 2번 -> 3번 차례로 접근하세요')

    elif select_no == 6:
        cvx.vaccine_drow_chart()
    elif select_no == 7:
        pass


if __name__ == '__main__':
    while True:
        select_n = menu()
        if select_n == 0:
            break
        select(select_n)
