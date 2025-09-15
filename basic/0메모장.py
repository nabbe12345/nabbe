#g =input()
#print('입력받은 숫자 : {g}')

# ' git  = 로컬 ,커밋 ,메인폴더 깃 추가 , 푸시'
# from itertools import count
# from os import remove
#
# a = [1,2,3,6,4,5,6,7,3,4,1,]
# idx = 0
#
# for i ,v in enumerate(a,idx):
#     if v == 3:
#         print(f'asfd : {i}')

#깃 원격관리 주소 추가


#
# def i(fire):
#     print(f'{fire}에 불이 켜집니다')
#     return f'{fire}가 켜졌습니다'
# dd = i('wow')
# print(dd)





menus = []

def menu():
    input(f'{menu}메뉴를 입력해주세요')
    menus.append(menu)
    while True:
     if menu == '끝':
        break
    return menus

oo = menu()
print(oo)


    #if input(f'결제 수단은 무엇입니까 ? cash / card'):




def menu():
    menus = []
    while True:
        item = input('메뉴를 입력해주세요: ')
        if item == '끝':
            break
        menus.append(item)
    return menus

oo = menu()
print(oo)









