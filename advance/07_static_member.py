#static 원본
#heap 복사본 저장 출석부 복사본 원본 수정시 윈본으로 가야한다 그걸 바꾸는게 메서드


class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')

    @classmethod # 원본영역의 변수를 건드릴수 있다는 표시
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

# 원본의 내용을 고치고 싶다면?  -> 원본으로 직접 가서 고쳐야한다
Robot.count = 1000
# 원본(static)을 수정해도 이미 복사본(heap) 영역에는 영향을 안받는다
# 영역이 다르다


print(f'r1.count : {r1.count}')
print(f'r2.count : {r2.count}')
r1.how_count()
r2.how_count()

#마찬가지로 원본의 내용을 확인하고 싶다면 원본영역으로 가서 확인해야 한다
# ex) 출석부 고치러 직접가야함
print(f'원본 count : {Robot.count}') #Robot영역에있는 .count
print(f'원본 함수 : {Robot.std_count()}') #Robot영역에 있는 .std_count()함수
#TypeError: Robot.std_count() missing 1 required positional argument: 'self'
# 셀프 어디갔어 ?????????????????????
Robot.std_count()
# 해결법 @classmethod를 추가해 원본에서 수정할꺼라는 명령어를 만들어준다
# 그러면 self를 안붙여도 에러가 안뜬다
# self = 복사본이니깐


#self = 이 객체 라는 것


