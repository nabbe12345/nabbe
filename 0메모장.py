import random
num = [int(random.randint(1,100)) for num in range(3)]
print(f'정답은{num}이야')

run = [False,False,False]
while not all(run):
    pick = int(input('내가 생각한 숫자는?'))
    print(f'입력한 값은 :{pick}')
    for x in range(3):
        if not run[x]:
            guess = int(input(f'{x+1}번째 숫자를 맞춰보세요 (1~100)'))
        if pass


g =input()
print(f'입력받은 숫자 : {g}')
