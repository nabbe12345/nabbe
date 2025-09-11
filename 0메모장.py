#g =input()
#print('입력받은 숫자 : {g}')

' git  = 로컬 ,커밋 ,메인폴더 깃 추가 , 푸시'
import random

numer = random.randint(1,4)
num = input()
print(f'{num}')

running = True
while running:
    if num == numer:
        running = False
    elif num < numer:
        print(