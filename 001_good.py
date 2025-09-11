a = [3,4,1,2,3,4,5,6,1,3,4,2,4]
start = 0
for n in a:
    if n == 4:
        print(f'4 가 있는 인덱스 : {start}')
    start += 1


a = [3,4,1,2,3,4,5,6,1,3,4,2,4]
start = 0
running = True
while running:
    start = a.index(4, start)
    print(f'4에 값은 {start}에 있다')
    start += 1
    if start == len(a):
        running = False

a = [3,4,1,2,3,4,5,6,1,3,4,2,4]

for i,v in enumerate(a):
    if v == 4:
        print(f'4에 값은 {i}입니다!')

for t,o in enumerate(a):
    if o ==3:
        print(f'3은 {t}에 있습니다')

#
