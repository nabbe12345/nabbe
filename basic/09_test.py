import random

#numer = random.randint(1,31)     #자동완성으로 import random
#print(f'내 마음속 숫자: {numer}')



# 입력받은 값을 정수(int)로 변환하여 guess 에 대입
#guess = int(input('1~31 중 내가 생각한 숫자는?'))         #input으로 받은건 문자로 인식
#print(f'입력받은 숫자 : {guess}')



#=====입력한 값과 결과값이 맞을때
#=====내가 생각보다 큰거 , 작은거를 출력


# while running:
 #pass뭐를 할지 모르겠어 처리하지마




# ========================================

numer = random.randint(1,31)                          #변수 number , guess ,running
print(f'내 마음속 숫자: {numer}')

running = True
while running:
    guess = int(input('1~31 중 내가 생각한 숫자는?'))
    print(f'입력받은 숫자 : {guess}')
    if guess == numer:                 #'만약에'
        running = False
    elif guess < numer:
        print(f'{guess}가 더 작습니다')
    elif guess > numer:
        print(f'{guess}가 더 큽니다')


# ==========================================
# num = random.randint(3,30)
# print(f'정답: {num}')

# ok = True
# while ok:
#     o = int(input('2 ~ 30 중 고르세요'))
#     print(f'입력받은 숫자: {o}')
#     if o == num:
#         running = False
#     elif o < num:
#         print(f'{o}가 더 큽니다')
#     elif o > num:
#         print(f'{o}가 더 작습니다')


# ===================================
numer = random.randint(1,31)    #numer 변수를 1~31까지 랜덤으로 나오는 실행문           #변수 number , guess ,running
print(f'내 마음속 숫자: {numer}')      #numer 변수속에 결과값                               #효율적인 코드

running = True  #running라는 변수에 Ture를 적어뒀다
while running:  #while라는 무한 반복의 명령어를 키고 끄는 스위치 역활의 변수가 running

    guess = int(input('1~31 중 내가 생각한 숫자는?'))
    #guess라는 변수에 input으로 받는건 문자로 인식하여 앞에 int를 쓰고 정수로 변경
    print(f'입력받은 숫자 : {guess}') # f를 입력하여 순서를 지정
    if guess > numer:                                          #'만약에'
        print('내가 생각한 숫자보다 작습니다')
    elif numer < guess:
        print('내가 생각한 숫자보다 큽니다')
    else:
        print('정답입니다')
        running = False   # if elif 조건이 다 안 맞을시 else으로 온다
        #else로 왔다는건 == 라는거니 running 변수는 false로 변환해 무한 루프를 종료한다


#while 은 오른쪽에 있는 조건 결과가 트루 일 경우 반복되는 구문




