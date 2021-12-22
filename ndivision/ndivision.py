import tkinter as tk
import copy

namenum = 0 #참가자 수
name = [] #참가자 이름 엔트리 리스트
name_lbl = [] #n번째 참가자 출력 레이블
ntime_lbl = [] #n차 가격 레이블
ntime_ent = [] #n차 가격 입력 엔트리
ntime_abs = [] #n차 '참가' 글씨 출력 엔트리

cal = {} #참가자 정보 체크 딕셔너리
chk_btn = {} #체크버튼 딕셔너리


cnt = []


#참가자 입력 버튼 눌렀을 때 실행되는 함수
def input_people():
    #변수 선언
    global input_finish #미리 생성한 계산 버튼
    global namenum #참가자 수
    global name #참가자 이름 엔트리 리스트
    global name_lbl #x번째 참가자 출력 레이블
    global ntime_lbl #n차금액 출력 레이블
    global ntime_ent #n차 가격 입력 엔트리
    
    num = 0
    warning_text = '''아래에 참가자들 이름 입력 후 가격 입력 버튼을 누르세요.
*중복되는 이름 사용 불가*'''
    lbl_space2['height'] = 3

    num = int(ent_people_num.get())
    input_finish.destroy() #계산버튼 위치를 바꿔주기 위해서 미리 만들고 함수 호출 시 삭제

    #레이블/엔트리 개수 초기화
    for i in range(namenum) :
        name[i].destroy()
        name_lbl[i].destroy()
    name = []
    name_lbl = []

#인원 수에 맞춰 리스트 2개 (레이블 리스트, 엔트리 리스트) 생성, 위젯 설정
    #리스트에 생성한 레이블, 엔트리 추가
    #참가자x 출력 레이블 + 이름 쓰는 엔트리 추가
    for i in range(num) :
        name.append("name"+str(i+1))
        name_lbl.append("name_lbl"+str(i+1))
        name_lbl[i] = tk.Label(win, text = "참가자" + str(i+1), width = 8, anchor = 's')
        name_lbl[i].grid(row = 3, column = i + 2)
        name[i] = tk.Entry(win, width = 7)
        name[i].grid(row = 4, column = i + 2)
    namenum = len(name)

    namewrite_lbl = tk.Label(win, text = "이름 :", anchor = 'e')
    namewrite_lbl.grid(row = 4, column = 1)
    btn_cash = tk.Button(win, text = "가격 입력", command = set_cash)
    btn_cash.grid(row = 4, column = i + 3)
    lbl_space3 = tk.Label(win, width = 1)
    lbl_space3.grid(row = 4, column = i + 4)
    lbl_space4.grid(row = 5, column = 1)
        
    #숫자가 음수나 0인 경우 경고 문구 출력    
    if int(ent_people_num.get()) <= 0 or int(ent_ntimes.get()) <= 0:
        warning_text = "위의 숫자 제대로 입력 하셨나요?"
        lbl_space2['anchor'] = 'n'
    lbl_space2['text'] = warning_text
    lbl_space2['anchor'] = 's'
    warning_text = '''아래에 참가자들 이름 입력 후 가격 입력 버튼을 누르세요.
*중복되는 이름 사용 불가*'''

    #btn_calculate = tk.Button(win, text = "가격 입력", width = 10, command = calculate)
    #btn_calculate.grid(row = int(ent_ntimes.get()) + 7, column = i + 2, columnspan = int(ent_ntimes.get()))


#엔트리에 적혀있는 값 삭제하는 내용
    #ent_people_num.delete(0, len(ent_people_num.get()))
    #ent_ntimes.delete(0, len(ent_ntimes.get()))
    

def set_cash():

    global ntime_abs #n차 '참가' 글씨 출력 엔트리
    
    lbl_space4['text'] = '금액'
    lbl_space4['anchor'] = 's'
    cal.clear() #딕셔너리 초기화
    chk_btn.clear()

    for i in range(int(ent_people_num.get())) :
        ntime_abs.append(i)
        ntime_abs[i] = tk.Label(win, text = "참가여부")
        ntime_abs[i].grid(row = 5, column = 2 + i)

    #n차 금액 입력하는 레이블/엔트리 추가
    for i in range(int(ent_ntimes.get())) :
        ntime_lbl.append(i)
        ntime_ent.append(i)
        ntime_lbl[i] = tk.Label(win, text = str(i+1) + " 차 :", anchor = 'e')
        ntime_ent[i] = tk.Entry(win, width = 7)
        ntime_lbl[i].grid(row = i + 6, column = 0)
        ntime_ent[i].grid(row = i + 6, column = 1)
        
    #참석자 명단:n차 참석 여부 값을 key:value로 저장할 딕셔너리 cal
    #체크박스 객체를 저장 할 딕셔너리 chk_btn
    for i in range(int(ent_people_num.get())) :
        instance = []
        instance2 = []
        for a in range(int(ent_ntimes.get())):
            instance.append(tk.IntVar())
            instance2.append(tk.IntVar())
        cal[name[i].get()] = instance
        chk_btn[name[i].get()] = instance2
    
    #체크박스 생성, variable를 cal 딕셔너리 value로
    for j in range(int(ent_people_num.get())) :
        for i in range(int(ent_ntimes.get())) :
            cal[name[j].get()][i].set(True)
            chk_btn[name[j].get()][i] = tk.Checkbutton(win, variable = cal[name[j].get()][i])
            chk_btn[name[j].get()][i].grid(row = 6 + i, column = 2 + j)

    btn_calc = tk.Button(win, text = "계산!", command = calculate)
    btn_calc.grid(row = 5 + int(ent_ntimes.get()), column = 2 + int(ent_people_num.get()))
    
    #이거는 계산 함수에서 바꿔줘야 함
    space_lb5 = tk.Label(win, height = 2, text = '1원 이하는 절삭하고 계산합니다.', anchor = 's', fg = 'red')
    space_lb5.grid(row = int(ent_ntimes.get()) + 7, column = 0, columnspan = int(ent_people_num.get()) + 3)


def calculate() :
    money = [] #n차별 총 금액
    ndivmoney = [] #n빵 금액
    cnt = [] #n차별 참여자 수
    calc_money = {} #n차별 내야하는 각각 금액
    calc_money.clear()
    names = []
    
    space_lb5['height'] = 3
    #리스트 초기화
    for i in range(int(ent_ntimes.get())) :
        money.append(int(ntime_ent[i].get()))
        cnt.append(0)
    for i in range(int(ent_people_num.get())) :
        instance = []
        for a in range(int(ent_ntimes.get())):
            instance.append(tk.IntVar())
            instance[a].set(0)
        calc_money[name[i].get()] = instance

    #n차 참여자 카운트
    for j in range(int(ent_ntimes.get())) :
        for i in range(int(ent_people_num.get())) :
            if cal[name[i].get()][j].get() == 1 :
                cnt[j] += 1

    #n차별 n빵금액 계산
    for i in range(int(ent_ntimes.get())) :
        ndivmoney.append(money[i]//cnt[i])
    
    
    #각각 n차마다 내야하는 금액 딕셔너리 추가
    for j in range(int(ent_ntimes.get())) :
        for i in range(int(ent_people_num.get())) :
            if cal[name[i].get()][j].get() == 1 :
                calc_money[name[i].get()][j] = ndivmoney[j]
            elif cal[name[i].get()][j].get() == 0 :
                calc_money[name[i].get()][j] = 0

    #결과 레이아웃
    names = list(calc_money.keys())
    lbl_result_name = [] #참가자 이름 출력 레이블
    lbl_times_result = [] #n차 + 총합 글씨 출력 레이블
    
    lbl_result = [] #n차별 각각의 금액이 출력되는 레이블
    lbl_result_show = [] #n차별 각각의 금액이 저장되는 리스트

    #n차 + 총합 글씨 출력
    for i in range(int(ent_ntimes.get()) + 1) :
        lbl_times_result.append(0)
    for i in range(int(ent_ntimes.get())) :
        lbl_times_result[i] = tk.Label(win, text = str(i+1) + '차')
        lbl_times_result[i].grid(row = int(ent_ntimes.get()) + 8, column = i + 1)
    lbl_times_result[i+1] = tk.Label(win, text = '총 합')
    lbl_times_result[i+1].grid(row = int(ent_ntimes.get()) + 8, column = i + 2)

    #참가 이름 출력
    for i in range(len(names)) :
        lbl_result_name.append(0)
        lbl_times_result.append(names[i])
        lbl_result_name[i] = tk.Label(win, text = names[i])
        lbl_result_name[i].grid(row = int(ent_ntimes.get()) + 9 + i, column = 0)

    #금액 계산 리스트 설정 및 모든 값 0으로 초기화
    for j in range(len(names)) :
        lbl_result.append([]) #레이블 리스트
        lbl_result_show.append([]) #금액 값 리스트
        for i in range(int(ent_ntimes.get()) + 1) :
            lbl_result[j].append(0)
            lbl_result_show[j].append(0)
    
    #금액 계산 j = 이름 // i = n차 // i+1 = 총 합
    for j in range(len(names)) :
        for i in range(int(ent_ntimes.get())) :
            lbl_result_show[j][i] = calc_money[name[j].get()][i]
        lbl_result_show[j][i + 1] = sum(calc_money[name[j].get()])
    
    #금액 출력
    for j in range(len(names)) :
        for i in range(int(ent_ntimes.get()) + 1) :
            lbl_result[j][i] = tk.Label(win, text = str(lbl_result_show[j][i]) + '원', relief = 'groove')
            lbl_result[j][i].grid(row = int(ent_ntimes.get()) + 9 + j, column = i + 1)
            
            #총 합은 굵은 테두리로
            if i == int(ent_ntimes.get()) :
                lbl_result[j][i]['relief'] = 'solid'
    space_lb7 = tk.Label(win, height = 1)
    space_lb7.grid(row = int(ent_ntimes.get()) + 10 + j, column = 0, columnspan = 2)
    lbl_sendnum = tk.Label(win, text = '    돈 보내실 곳', height = 1)
    lbl_sendnum.grid(row = int(ent_ntimes.get()) + 11 + j, column = 0, columnspan = 2)
    ent_sendnum = tk.Entry(win, width = 30)
    ent_sendnum.grid(row = int(ent_ntimes.get()) + 11 + j, column = 2, columnspan = 10)
    lbl_space6 = tk.Label(win, height = 1, justify = 'left')
    lbl_space6.grid(row = int(ent_ntimes.get()) + 12 + j, column = 1, columnspan = 5)


    
win = tk.Tk()

win.title("N빵 계산기")
win.resizable(width=True, height=True)
win.geometry("+600+200")

#여러 함수에서 쓰는 위젯 미리 선언
input_finish = tk.Button()
lbl_space4 = tk.Label(win, height = 1)
space_lb5 = tk.Label(win, height = 1, text = '계산 결과 나오는 자리', anchor = 'center')

#1행 (레이블-엔트리-빈레이블-공백-빈레이블)
lbl_people_num = tk.Label(win, text = "몇 명? ", width = 6, anchor = 'w')
lbl_people_num.grid(row = 0, column = 0)
ent_people_num = tk.Entry(win, width = 7)
ent_people_num.grid(row = 0, column = 1)
lbl_people_num_back = tk.Label(win, text = "명이서", width = 8, anchor = 'w')
lbl_people_num_back.grid(row = 0, column = 2)

#2행 (레이블-엔트리-공백-버튼-공백)
lbl_ntimes = tk.Label(win, text = "몇 차? ", width = 6, anchor = 'w')
lbl_ntimes.grid(row = 1, column = 0)
ent_ntimes = tk.Entry(win, width = 7)
ent_ntimes.grid(row = 1, column = 1)
lbl_space = tk.Label(win, text = "차까지", width = 8, anchor = 'w')
lbl_space.grid(row = 1, column = 2)
btn_people_num = tk.Button(win, text = "참가자 입력", padx = 5, command = input_people)
btn_people_num.grid(row = 1, column = 3, columnspan = 3)

#3행 (경고 문구 레이블 - 수평확장)
lbl_space2 = tk.Label(win, height = 2, fg = 'red', anchor = 's')
lbl_space2.grid(row = 2, columnspan = 10)


win.mainloop()
