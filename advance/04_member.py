class Robot:

    # 생성자 : 객체화 할때 호출되는 함수의 일종으로
    # 객체화가 될때 가장 먼저 호출된다
    # ex)Robot()을 호출 할때 init이 호출

    def __init__(self):
        #초기화를 한다 (최초의 값을 주어준다)
        # ex)강아지 이름 / 목적:우리집을 잘 지켜
        print('Robot 이 복사될때 제일 먼저 호출 되는 멤버')

    def doIt(self):
        print('나는 Robot 의 함수 입니다')

robot = Robot()
robot.doIt()

#robot = Robot() 으로 객체화 요청 -> 생성자 호출(init) -> 객체화
