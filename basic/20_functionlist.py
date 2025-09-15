# 반환타입: O 매개변수: O         토스트기 , 인형뽑기,커피그라인더
# 반환타입: O 매개변수: X         번호표   ,
# 반환타입: X 매개변수: O         모금함   , 오락실게임
# 반환타입: X 매개변수: X         호출벨


# dish = toaster('빵')
# print(dish)
#
# def toaster(bread):
#     print(f'{bread}이 구워지고 있다')
#     return f'구워진 {bread}'


#인형뽑기 :반환타입: O 매개변수: O



def dd(coin): #선언 : 만들어만놨지 누가 사용한건 아님
    print(f'{coin}으로 인형이 뽑고 있다')
    return f'{coin}으로 뽑은 티니핑 인형'

dol = dd('1000원')
print(dol)                       #my




def 토스트기(bread):           #선언 : 만들어만놨지 누가 사용한건 아님
    print(f'{bread}이 구워진다')    #실질적 동작이 아님 , 사람 눈에만 보임
    return f'구워진{bread}'        # 실제로 밖으로 나오는 값

#사용

dish = 토스트기('종이') # return 으로 나온 값을 dish에 담는다
print(dish) #dish 안의 값을 출력

print(토스트기('감자')) #토스트기에서 나온 값을 바로 출력



def 그라인더(been):
    print(f'{been}가 갈리고 있다')
    return f'곱게 갈린 {been}'


package =그라인더('아라비카 원두')
print(package)


#번호표 :반환타입: O 매개변수: X



num = 3
def i():
    return f'{num} 번째 번호표'
print(i())                        #my



def 번호표기계():
    return  "번호표"

print(번호표기계())




def 모니터():
    return "꺼진 모니터"

print(모니터())

#오락실게임 :반환타입: X 매개변수: O            return X

#def game(coin):
#     print(f'{coin}번 게임 시작')

#    good = game('4')
#    print(good)                       #my



def 저금통(coin):
    print(f'{coin}원 저축')

저금통(500)



def 모금함(coin):
    print(f'{coin}원을 기부 했다')

모금함(5000)


#print(저금통()) <- X
# 저금통에는 return이 없는데
# 저금통 실행후 나온값을 출력하려고 하니
# None 이 출력 되는 것







#호출벨 :반환타입: X 매개변수: X

#def ring():
#    print('벨이 울렸습니다')
#print(ring())                  #my



def 호출벨():
    print('호출벨이 울린다')

호출벨()         #none 튀어나온걸 출력


def 꺼진휴대폰():
    print('휴대폰이 꺼져있다')

꺼진휴대폰()

#인자값 /parameter / 매개변수 / 레퍼런스(참조)변수          모두 같은 말

#list
#dic
#set

