#tuple 수정 삭제 x
# [] 말고 ()로 선언

tu1 = (1,2,3)
tu2 = ('a','b','c')
tu3 = (1,2,('a','b'))   # 2차원 튜블


# 불러오기는 [] 사용
print(tu1[1])
# slicing
print(tu2[1:])
# 더하기
print(tu1+tu2)
# 곱하기
print(tu1*3)


#tuple <-------> list 간의 전환
tu2list = list(tu2)          #list 함수를 이용
print(f'{tu2} -> {tu2list}')     # 튜플에서 리스트로 변환

list2tu = tuple(tu2list)     #tuple 함수 이용
print(f'{tu2list} -> {list2tu}')   #리스트에서 튜플로 변환


