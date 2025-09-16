class Car:
    #멤버 변수(필드)
    gear = 0
    on = False

    # 생성자 init - 클래스는 사용시 객체화를 하기 때문에 생성자는 필수다
    # 그런데 프로그래밍의 규칙중 하나는 너무 당연하게 있어야 할것들은 생략이 가능하다
    def __init__(self):
        # 혹시나 기어가 들어가 있거나 시동이 켜있을수 있어서 초기 상태로 되돌려 놓는다
        self.gear = 0
        self.on = False
    #세팅 하는것

    # 멤버 함수 - 클래스 안의 생성자 함수들은 해당 객체를 표시하기 위한 self를 기본으로 가지고 있는다
    def start(self):
        if self.on == False:      # 시동이 꺼지면 출력
            print('시동이 걸렸습니다')
            self.on = True        # 시동을 진짜 키는것
        else:
          print('시동이 이미 걸려있습니다')

    def change(self,gear):    #매개변수를 추가하여
        print(f'{gear} 단으로 변속 했습니다') # '받아온 값으로'
        self.gear += gear          # gear 가 self.gear로 들어가서 +1 해준다
                                   # 1단 2단 3단
        
        
# Car 클래스를 객체화(복사)
# 객체를 통해 사용하고 싶은 멤버 호출
car = Car()      #Car에서 복사한 car라는 변수
# 시동 걸기
car.start()      # 맴버 함수
# 변속 하기
car.change(3)
print(f'현재 car 의 gear 단수 : {car.gear}')
# 출력은 car.gear로 한다
# 왜냐면 Car라는 함수를 car에 담았기 때문 (복사본)

