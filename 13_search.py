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











