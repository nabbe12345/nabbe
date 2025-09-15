cup = 0

running =True

while running:
    cup += 1
    print(cup)
    if cup == 10:           #출력 할 필요가 없는 조건
        #running = False    # running 변수를 false로 변환해서 해결
        break               #조건을 만족하여 브레이크라는 해결

print('while 문 종료')

#==============================================


#continue = 도돌이표

for i in range(1,10):
    if i == 3:            #만약 i가 3이라는 조건일시
        continue          #무시하고 다시 for로 간다 단 3은 제외
    print(i)


for t in range(1,11):
    if t == 3:             # 메인 if에 추가 if를 연속적으로 들어가면 continue 고장남*
        continue
    if t == 6:
        continue
    if t == 9:
        continue
    print(t)

    if t % 3 == 0:    # 나머지 연산으로 9를 3으로 나눈후 값이 0 인것
        continue
