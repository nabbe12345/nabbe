import traceback

num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0

try:
    while True:
        idx = num_list.index(3,idx) # ValueError: 3 is not in list
        print(f'3 은 {idx} 인덱스에 있습니다.')
        idx += 1     # while 문을 멈추는 법이 없다
except ValueError as e:     #에러 확인하는 법 일반적으로는 사용 안함
    print(e) # 예외에 대한 대략적인 정보 출력
    traceback.print_exc() # 꼭 자동완성 (임포트가 적힘) 
    # 상세한 예외 정보 (개발자에게 필요한 정보 : 내가 아는 빨간 에러)
    print('더 이상 3을 찾을 수 없습니다')
finally:
    print('@@@@@@@@@@@@@@@@@@@끝@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

'''들여쓰기 신경쓰기 '''

