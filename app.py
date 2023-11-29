import streamlit as st
import numpy as np
from itertools import permutations
import random


# 각 자리수가 중복되지 않는 난수 생성

# 난수3개 생성 
def randnum1():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #각 자리수
    nums = list(permutations(digits, 3))    #위 리스트에서 3자리 숫자뽑기 => nums 에 list형태로 저장
    random.shuffle(nums)    #nums 무작위로 섞음
    return nums[0]  #난수 리턴 

# 난수4개 생성
def randnum2():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #각 자리수
    nums = list(permutations(digits, 4))    #위 리스트에서 4자리 숫자뽑기 => nums 에 list형태로 저장
    random.shuffle(nums)    #nums 무작위로 섞음
    return nums[0]  #난수 리턴 

# 난수5개 생성
def randnum3():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] #각 자리수
    nums = list(permutations(digits, 5))    #위 리스트에서 5자리 숫자뽑기 => nums 에 list형태로 저장
    random.shuffle(nums)    #nums 무작위로 섞음
    return nums[0]  #난수 리턴 

################################################################################################################################################################

# 게임 결과 출력 함수

def result1(input, ball, strike):       #입력값, ball,strike 를 매개변수로 넘겨받음
    if strike == 3:
        st.write('# Victory')           #strike가 3 == 승리
    elif st.session_state.inning >= 15:
        st.write('# Gameover')          #시도횟수가 15회 제한
        st.write('정답은 ', str(st.session_state.randnums[0]) + str(st.session_state.randnums[1]) + str(st.session_state.randnums[2]), ' 입니다.')  #정답출력
        st.write('새로운 게임을 하시려면 F5를 눌러주세요.')

    else:
        for i in range(st.session_state.inning + 1):    #게임의 진행횟수만큼 반복문 실행
            st.session_state.record.append([])          #게임의 기록을 저장하기 위해 빈 배열 생성
            st.session_state.record[i].append([])       #각회차마다의 정보를 기록하기위해 2차원 배열 생성
            st.session_state.record[i].append(input)    #입력값
            st.session_state.record[i].append(ball)     #볼
            st.session_state.record[i].append(strike)   #스트라이크

            #각 회차마다의 기록을 저장하여 출력
            st.write(i + 1, '회 입력숫자: ', st.session_state.record[i][1], st.session_state.record[i][2],' ball ', st.session_state.record[i][3], ' strike ')  
            

def result2(input, ball, strike):                       #입력값, ball,strike 를 매개변수로 넘겨받음
    if strike == 4:
        st.write('# Victory')                           #strike가 4 == 승리
    elif st.session_state.inning >= 15:
        st.write('# Gameover')                          #시도횟수가 15회 제한
        st.write('정답은 ', str(st.session_state.randnums[0]) + str(st.session_state.randnums[1]) + str(st.session_state.randnums[2])
                 +str(st.session_state.randnums[3]), ' 입니다.')  #정답출력
        st.write('새로운 게임을 하시려면 F5를 눌러주세요.')

    else:
        for i in range(st.session_state.inning + 1):    #게임의 진행횟수만큼 반복문 실행
            st.session_state.record.append([])          #게임의 기록을 저장하기 위해 빈 배열 생성
            st.session_state.record[i].append([])       #각회차마다의 정보를 기록하기위해 2차원 배열 생성
            st.session_state.record[i].append(input)    #입력값
            st.session_state.record[i].append(ball)     #볼
            st.session_state.record[i].append(strike)   #스트라이크

            #각 회차마다의 기록을 저장하여 출력
            st.write(i + 1, '회 입력숫자: ', st.session_state.record[i][1], st.session_state.record[i][2],' ball ', st.session_state.record[i][3], ' strike ')  

def result3(input, ball, strike):                       #입력값, ball,strike 를 매개변수로 넘겨받음
    if strike == 5:
        st.write('# Victory')                           #strike가 5 == 승리
    elif st.session_state.inning >= 15:
        st.write('# Gameover')                          #시도횟수가 15회 제한
        st.write('정답은 ', str(st.session_state.randnums[0]) + str(st.session_state.randnums[1]) + str(st.session_state.randnums[2])
                 +str(st.session_state.randnums[3])+str(st.session_state.randnums[4]), ' 입니다.')  #정답출력
        st.write('새로운 게임을 하시려면 F5를 눌러주세요.')

    else:
        for i in range(st.session_state.inning + 1):    #게임의 진행횟수만큼 반복문 실행
            st.session_state.record.append([])          #게임의 기록을 저장하기 위해 빈 배열 생성
            st.session_state.record[i].append([])       #각회차마다의 정보를 기록하기위해 2차원 배열 생성
            st.session_state.record[i].append(input)    #입력값
            st.session_state.record[i].append(ball)     #볼
            st.session_state.record[i].append(strike)   #스트라이크

            #각 회차마다의 기록을 저장하여 출력
            st.write(i + 1, '회 입력숫자: ', st.session_state.record[i][1], st.session_state.record[i][2],' ball ', st.session_state.record[i][3], ' strike ')  

#####################################################################################################################################################################

# 입력 받은 값을 매개변수로 하여 검증 함수

def verify_digit1(input):
    strike = 0
    ball = 0
    randnums = st.session_state.randnums     #Streamlit 애플리케이션에서 사용되는 상태 변수 randnums를 가져옴
    
    #입력받은값은 문자열이므로 각 인덱스와 정답의 각 인덱스와 비교
    for i in range(len(randnums)):  
        if i < len(input) and randnums[i] == input[i]:      #자리,숫자 둘다 일치 => strike
            strike += 1     
        elif i < len(input) and input[i] in randnums:    #숫자만 일치 => ball 
            ball += 1        

    result1(input, ball, strike)

def verify_digit2(input):
    strike = 0
    ball = 0
    randnums = st.session_state.randnums     #Streamlit 애플리케이션에서 사용되는 상태 변수 randnums를 가져옴
    
    #입력받은값은 문자열이므로 각 인덱스와 정답의 각 인덱스와 비교
    for i in range(len(randnums)):  
        if i < len(input) and randnums[i] == input[i]:      #자리,숫자 둘다 일치 => strike
            strike += 1     
        elif i < len(input) and input[i] in randnums:    #숫자만 일치 => ball 
            ball += 1        

    result2(input, ball, strike)

def verify_digit3(input):
    strike = 0
    ball = 0
    randnums = st.session_state.randnums     #Streamlit 애플리케이션에서 사용되는 상태 변수 randnums를 가져옴
    
    #입력받은값은 문자열이므로 각 인덱스와 정답의 각 인덱스와 비교
    for i in range(len(randnums)):  
        if i < len(input) and randnums[i] == input[i]:      #자리,숫자 둘다 일치 => strike
            strike += 1     
        elif i < len(input) and input[i] in randnums:    #숫자만 일치 => ball 
            ball += 1        

    result3(input, ball, strike)
    
###################################################################################################################################################################

# <게임시작>

# TITTLE
st.header('_숫자 야구 게임_ :baseball:', anchor='center')

# 난이도 선택
add_selectbox = st.sidebar.selectbox(
    "난이도 선택",
    ("초급", "중급", "상급"),
    key='difficulty_selectbox'
)


#초급

if add_selectbox == '초급':


    #스트림릿의 새로고침 오류 보안

    def run_easy_game():
        if 'number' not in st.session_state:        #streamlit의 구조상 상호작용을 할때마다 새로고침되므로 변수에 저장된 값이 사라지지 않기 위해 작성
            st.session_state.number = []            #number 변수를 빈 리스트로 초기화 
        if 'i' not in st.session_state:             #for문에 사용되는 변수 i
            st.session_state.i = 0                  #초기화
        if 'randnums' not in st.session_state:      #난수
            st.session_state.randnums = randnum1()  #randnums에 난수로 초기화
        if 'inputNum' not in st.session_state:      #입력받은 숫자
            st.session_state.inputNum = ""          #초기화
        if 'inning' not in st.session_state:        #시도횟수
            st.session_state.inning = 0             #초기화
        if 'record' not in st.session_state:        #게임 진행 기록
            st.session_state.record = []            #초기화

        st.write('초급')
        

        # 버튼누름 => 규칙설명
        if st.button('게임 규칙'):
            st.write('숫자야구는 0부터 9까지의 각 자리의 수가 다른 3자리의 숫자를 추리하는 게임입니다.')
            st.write('1. 숫자는 맞지만 위치가 틀렸을때는 :blue[Ball]')
            st.write('2. 숫자와 위치 모두 일치할 경우 :green[Strike]')
            st.write('3. 숫자와 위치 모두 틀렸을 경우 :red[Out]')
            st.write('4. 15번의 시도 후 정답을 맞히지 못한다면 :rainbow[Gameover] 입니다.')
            st.write('5. 초기화 하고 싶으면 F5를 누르세요.')

            st.session_state.inning -= 1        #버튼 글릭시 시도횟수가 증가하는 버그 해결
            if st.session_state.inning < 1:     #위 버그 해결후 처음 버튼클릭시 시도횟수가 -1,0 이 되는 버그 해결
                st.session_state.inning = 1     #버그 해결

        input = st.text_input("012부터 987 사이의 숫자 3개를 입력하세요 ", max_chars=3)     #최대 3자리 수만 입력
        if input:         #input의 초기값은 빈 문자열 (False) => 입력이 되었을때 (True) 아래의 내용 실행
            if len(input) == 3 and input.isdigit() and '012' <= input <= '987':     #3자리의 입력 / 숫자만 입력 / 012~987입력 
                st.session_state.inputNum = input       #입력받은값을 inputNum에 저장
                verify_digit1(input)                    #값을 입력받으면 검증실행
                st.session_state.inning += 1            #시도횟수 +1

            else:         #입력이 유효하지 않을경우 오류 출력
                st.error('012부터 987 사이의 3자리 숫자만 입력하세요.')

    run_easy_game()

#input>='012' and input<='987'이 문자열 사이에서도 정상작동 : 문자열도 ascii 코드 값에 따라 비교연산을 하기 떄문 


#중급

elif add_selectbox == '중급':
    def run_medium_game():
        if 'number' not in st.session_state:
            st.session_state.number = []
        if 'i' not in st.session_state:
            st.session_state.i = 0
        if 'randnums' not in st.session_state:
            st.session_state.randnums = randnum2()
        if 'inputNum' not in st.session_state:
            st.session_state.inputNum = ""
        if 'inning' not in st.session_state:
            st.session_state.inning = 0
        if 'record' not in st.session_state:
            st.session_state.record = []

        st.write('중급')

        # 버튼누름 => 규칙설명
        if st.button('게임 규칙'):
            st.write('숫자야구는 0부터 9까지의 각 자리의 수가 다른 4자리의 숫자를 추리하는 게임입니다.')
            st.write('1. 숫자는 맞지만 위치가 틀렸을때는 :blue[Ball]')
            st.write('2. 숫자와 위치 모두 일치할 경우 :green[Strike]')
            st.write('3. 숫자와 위치 모두 틀렸을 경우 :red[Out]')
            st.write('4. 15번의 시도 후 정답을 맞히지 못한다면 :rainbow[Gameover] 입니다.')
            st.write('5. 초기화 하고 싶으면 F5를 누르세요.')

            st.session_state.inning -= 1
            if st.session_state.inning < 1:
                st.session_state.inning = 1

        input = st.text_input("0123부터 9876사이의 숫자 4개를 입력하세요 ", max_chars=4)    #최대 4자리 수만 입력
        if input:
            if len(input) == 4 and input.isdigit() and '0123' <= input <= '9876':
                st.session_state.inputNum = input
                verify_digit2(input)
                st.session_state.inning += 1
            else:
                st.error('0123부터 9876사이의 4자리 숫자만 입력하세요.')

    run_medium_game()


#상급

elif add_selectbox == '상급':
    def run_advanced_game():
        if 'number' not in st.session_state:
            st.session_state.number = []
        if 'i' not in st.session_state:
            st.session_state.i = 0
        if 'randnums' not in st.session_state:
            st.session_state.randnums = randnum3()
        if 'inputNum' not in st.session_state:
            st.session_state.inputNum = ""
        if 'inning' not in st.session_state:
            st.session_state.inning = 0
        if 'record' not in st.session_state:
            st.session_state.record = []

        st.write('상급')

        # 버튼누름 => 규칙설명
        if st.button('게임 규칙'):
            st.write('숫자야구는 0부터 9까지의 각 자리의 수가 다른 5자리의 숫자를 추리하는 게임입니다.')
            st.write('1. 숫자는 맞지만 위치가 틀렸을때는 :blue[Ball]')
            st.write('2. 숫자와 위치 모두 일치할 경우 :green[Strike]')
            st.write('3. 숫자와 위치 모두 틀렸을 경우 :red[Out]')
            st.write('4. 15번의 시도 후 정답을 맞히지 못한다면 :rainbow[Gameover] 입니다.')
            st.write('5. 초기화 하고 싶으면 F5를 누르세요.')

            st.session_state.inning -= 1
            if st.session_state.inning < 1:
                st.session_state.inning = 1

        input = st.text_input("01234부터 98765사이의 숫자 5개를 입력하세요 ", max_chars=5)  #최대 5자리 수만 입력
        if input:
            if len(input) == 5 and input.isdigit() and '01234' <= input <= '98765':
                st.session_state.inputNum = input
                verify_digit3(input)
                st.session_state.inning += 1
            else:
                st.error('01234부터 98765사이의 5자리 숫자만 입력하세요.')

    run_advanced_game()