#g =input()
#print('입력받은 숫자 : {g}')
from operator import index

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





#menus = []

#def menu():
# while True:
 #  item = input('메뉴를 입력해주세요') #1 메뉴를 입력 주문받기
 #  if item == '끝': #2 연속적으로 주문받기 (반복)
 #   break #3 끝이라고 말하면 주문 그만 받기
 #   menus.append(item)
 # return menus
#4 결제는 카드 아니면 현금이냐고 물어보기

# card = '카드'
# cash = '현금'
# oo = menu()
# print(oo)

#1 메뉴를 입력 주문받기
#2 연속적으로 주문받기 (반복)
#3 끝이라고 말하면 주문 그만 받기
#4 결제는 카드 아니면 현금이냐고 물어보기
#5 ex)카드라면 카드로 결제 했다는 문장 출력하기
#6 메뉴 입력받은 값을 최종 값으로 출력하기 ex)아메리카노 ,카페라떼등등



    #if input(f'결제 수단은 무엇입니까 ? cash / card'):



#
# from memooooooooooo.Study import school
# print(f'공부: {school.study} / {school.book}')
#
#

#
# age = 40
# years = 2022
#
# def solution(age):
#     old = (years-age)
#     old += 1
#
#     return old
#
# print(solution(age))
#

#
# def solution(angle):
#     if angle < 90:
#         return 1
#     elif angle == 90:
#         return 2
#     elif angle < 180:
#         return 3
#     else:
#         return 4
#

#
# def solution(n, k):
#     ho = (n*12000) + ((k - (n//10))*2000)
#     return ho

#
# def solution(n):
#     if n % 7 ==0:
#         ok = n / 7
#     else:
#         ok = n//7 + 1
#     return ok



#numbers= [1,2,9,4,5,6,8,5]

#numbers.sort()
#print(numbers[-1]*numbers[-2])

#
# n= [1,52,87,4,58,6,65,34,21,10]
# # def solution(n):
# #     for item in n.index(-1):
# #
# #         print(n)
#
#
#
# def solution(n):
#     total = 0
#     for item in n:
#         total += item
#     return total
#
# total = solution(n)
# print(total)
#









# 반 전체 키가 담긴 정수 배열 array
# 머쓱이의 키 height
# 머쓱이보다 키 큰 사람 수를 return
# 키가 큰 사람 수를 만드는법


# array=[149, 180, 192, 170]
# height= 167
# result = 3



# array = [149, 180, 192, 170]
# height = 167
#
# def solution(array, height):
#     okk=0
#     for ok in array:
#         if ok > height:
#             okk += 1
#         else:
#             pass
#     return okk
#


'''
선분 세개로 삼격형을 만들기

조건: 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야함

삼각형의 세 변의 길이가 담긴 배열= sides
세 변으로 삼각형을 만들 수 있다면 1 아니면 2를 return

sides 길이는 3개 [1,2,3]

'''

sides = [6,10,6] # 이건 가능
#side= [3,2,6]   이건 불가능
# def solution(sides):
#     answer = 0
#     for item in sides:
#
#     return answer


def solution(sides):
    x = sides[2]
    y = sides[0]
    z = sides[1]
    if x>(y+z):
        i = 1
    else:
        i = 2
    return i
'''
sides에 제일 큰값을 구하기
sides에 두 수를 더하기
sides에 제일 큰값 보다 더한값이 더 크게 해야 만들수있다 리턴값 1
아니면 2

'''












