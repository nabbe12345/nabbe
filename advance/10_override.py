class Car:
    def start(self):
        print('시동이 걸린다')


    def run(self):
        print('차가 시속 50km 로 달린다')


    def stop(self):
        print('차가 멈춘다')


class MyCar(Car):

    turbo = False

    def run(self):    # '부모와 같은 메서드를 사용하면 오버라이드로 인식'
        if self.turbo == True:
         print('차가 시속 200km 로 달린다')
        else:
         super().run() # 부모의 run을 그대로 쓰겠다

mc = MyCar()       #MyCar를 객체화
mc.start()         #Car에서 가져옴


mc.run()           # 오버라이드
mc.turbo = True   # 오버라이드 상태지만 '부모것을 사용 할수있게 하는것'
mc.run()           # 오버라이드


mc.stop()          #Car에서 가져옴

