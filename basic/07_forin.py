# for문은 반복 횟수가 정해진 상태에 적합하다

# 물 10잔 떠오기
#for [하나씩 가져올 변수] in [범위]:       range = 몇부터 몇까지 가져오는
for cup in range(1, 11):                     # 개발의 시작은 모든 0 에서 부터 시작, 1 ~ 11이 맞는 표기
    print(f'물 {cup}번째 잔 떠왔습니다')



                                                      # 반복안에 반복이 가능
# 만약 커피를 타는데 한잔의 물에 믹스 2개씩을 넣어야 한다면?
# 반복안에 반복이 발생된다 == 이중 for문


for cup in range(1, 11):                        #for mix in range(1, 3):
    print(f'커피 {cup}번째 타왔습니다')            #    print(f'{mix}개 넣었습니다')



for cup in range(1, 11):
    print(f'커피 {cup}번째 타왔습니다')
    for mix in range(1, 3):
        print(f'{mix}개 넣었습니다')
    # =======줄바꿈 중요*        'for문에 포함 시킬지 새로운 for문을 만들지'


for cup in range(1, 11): #10번
    print(f'커피 {cup}번째 타왔습니다')
    for mix in range(1, 3): #2번
        print(f'믹스커피를 {mix}개 넣었습니다')
        for spoon in range(1, 4): #3번
            print(f'수푼으로 {spoon}번 섞는다')



