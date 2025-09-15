import oper


print(dir(oper))
#dir() 나장함수를 사용하면 모듈에 정의되어있는 변수, 함수 목록을 볼 수 있다.
# __ 2개는 파이썬이 만들어준 속성


#모듈의 이름 확인
print(oper.__name__) #특정 모듈의 이름을 확인하는것
print(__name__) #현재 나의 이름 -> 현재 실행되는 함수

