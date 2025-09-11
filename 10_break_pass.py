cup = 0

running =True

while running:
    cup += 1
    print(cup)
    if cup == 10:           #출력 할 필요가 없는 조건
        #running = False    # running 변수를 false로 변환해서 해결
        break               #조건을 만족하여 브레이크라는 해결

print('while 문 종료')