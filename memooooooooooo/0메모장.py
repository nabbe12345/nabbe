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
 while True:
   item = input('메뉴를 입력해주세요') #1 메뉴를 입력 주문받기
   if item == '끝': #2 연속적으로 주문받기 (반복)
    break #3 끝이라고 말하면 주문 그만 받기
   menus.append(item)
 return menus
#4 결제는 카드 아니면 현금이냐고 물어보기


#1 메뉴를 입력 주문받기
#2 연속적으로 주문받기 (반복)
#3 끝이라고 말하면 주문 그만 받기
#4 결제는 카드 아니면 현금이냐고 물어보기
#5 ex)카드라면 카드로 결제 했다는 문장 출력하기
#6 메뉴 입력받은 값을 최종 값으로 출력하기 ex)아메리카노 ,카페라떼등등






card = '카드'
cash = '현금'
oo = menu()
print(oo)


    #if input(f'결제 수단은 무엇입니까 ? cash / card'):




#def menu():
#    menus = []
#    while True:
#        item = input('메뉴를 입력해주세요: ')
#        if item == '끝':
#            break
#        menus.append(item)
#    return menus

#oo = menu()
#print(oo)









