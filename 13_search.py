# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는것
a = [3,4,1,2,3,4,'G','F','G']
# 원하는 값의 인덱스 찾기
# '2'라는 값을 어느 위치에 있는가?
print(f'2는 어디? : {a.index(2)}')     # 변수.index(찾으려는 값)
print(f'G는 어디? : {a.index('G')}')   # G 는 2개 이지만 처음 찾은 값만 알려준다
print(f'G는 어디? : {a.index('G',5)}')  # 5번 인덱스부터 'G'를 찾아라
        # index(찾으려는값,~ 부터 시작)

# print(a.index('H')) ValueError: 'H' is not in list
# 값이 없으면 에러(예외)를 발생 시킨다


b = [3,4,1,2,3,4,5,6,1,3,2] # 모든 3을 찾아 보세요
# print(f'3의 값은? : {b.index(3)}')
# print(f'3의 값은? : {b.index(3,1)}')
# print(f'3의 값은? : {b.index(3,5)}')

idx = 0
# while True:
#     idx = b.index(3,idx)  # 인덱스 3번을 0번 부터 찾으라는뜻
#     print(f'3의 값은 {idx}번에 있다') # 0이니 무한루프
#     idx += 1  # 그래서 1씩 증가



for n in b:                    #for in 을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    idx += 1

# 리스트 요소 삭제
# del a[3] 과 a.remove(3)
# del 은 특정 인덱스의 값을 지운다
# remove 는 해당 값을 지운다 (한개만) 첫 값만 지운다
print(f'a : {a}')
a.remove(3)
print(f'a : {a}')

#===================================



# pop() = append() 의 반대 개념
# 맨마지막 요소를 빼낸다  (리스트에서는 사라진다)

val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')
# 티슈 뽑는 원리
val = a.pop()
                                  ######print(f'{val} {a}') >?????

#====================================

# 리스트 확장(더하기와 비슷한 개념)       변수.extend()
a.extend(b)
print(a)


#====================================


#count(val) 특정한 값이 해당 리스트에 몇개 있는지 확인
print(a)
print(f'a 안에 3인 {a.count(3)} 개 가 있다')
print(f'a 안에 9인 {a.count(9)} 개 가 있다') # 없는 값은 0을 반환




# a 안에 있는 모든 3을 지워 주세요


# re = 0
# for h in a:
#     if re == 3:
#         print(f'a : {a}')
#     else:
#         del a[3]
#         print(f'a : {a}')



# while True:
#     re = a.index(1, re)
#     print(f'{a}')
#     del a[3]
#     print(f'a : {a}')


                            #for문 예시
for n in a:                 #for 변수 in 리스트변수
    if n ==3:               # 조건을 건다 '변수가 3이랑 같을때'
        a.remove(3)         # a의 3이 없을때까지 지운다 (앞에서 부터)
        print(a)


while True:                 #while문 예시
    a.remove(3)             #먼저 지우고
    if a.count(3) == 0:     #조건을 건다   '3 이 0이 될때까지'
        break               #0이 된다면 멈춘다
print(a)









