class Puppy:
#Puppy 맴버는 name,goal< 변수 init이라는 생성자

    name='' #멤버 변수(필드) : class 안에서 사용 가능한 변수
    goal=''

    def __init__(self,name,goal): # 생성자 : 객체화시 호출되는 '일단은 함수'
        pass


puppy = Puppy('멍멍이','집지키기')