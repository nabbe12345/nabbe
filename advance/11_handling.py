num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0

try:
    while True:
        idx = num_list.index(3,idx) # ValueError: 3 is not in list
        print(f'3 은 {idx} 인덱스에 있습니다.')
        idx += 1
except ValueError as e:     #에러를 확인하려면 as 변수 : 를 지정해서 프린트
    print(e) # 예외에 대한 대략적인 정보 출력
    print('더 이상 3을 찾을 수 없습니다')
finally:
    print('@@@@@@@@@@@@@@@@@@@끝@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

'''들여쓰기 신경쓰기 '''

