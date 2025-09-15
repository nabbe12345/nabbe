cup = 0

""" 조건이 무조건 참이될 경우 영원히 실행 되므로 멈출수 없다
while True:
    cup = cup+1
    print(cup)
"""

while cup<10:      #변수가 0일때 무한 반복 = ture랑 같음
    cup = cup + 1
    print(cup)

while True:
    i = 5
    if i == 10:
        break
    print(i)
