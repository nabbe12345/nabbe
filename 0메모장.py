#g =input()
#print('입력받은 숫자 : {g}')

' git  = 로컬 ,커밋 ,메인폴더 깃 추가 , 푸시'
from itertools import count
from os import remove

a = [1,2,3,6,4,5,6,7,3,4,1,]
idx = 0

for i ,v in enumerate(a,idx):
    if v == 3:
        print(f'asfd : {i}')

#깃 원격관리 주소 추가



def i(fire):
    print(f'{fire}에 불이 켜집니다')
    return f'{fire}가 켜졌습니다'
dd = i('wow')
print(dd)


a = [1,2,3,6,4,5,6,7,3,4,1,]
while True:
    a.remove(3)
    if a.count(3) == 0:
        break
    print(a)















