#static 원본
#heap 복사본 저장 출석부 복사본 원본 수정시 윈본으로 가야한다 그걸 바꾸는게 메서드


class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')


    def std_count(self):
        print(f'클래스 메서드 : {self.count}')


r1 = Robot()
r2 = Robot()     #지금 복사본이 2개 있다
#서로 다른 복사본이니 count를 건드렸을때 서로 영향 받지 않음



r1.count += 1
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r2.count = 100
print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
