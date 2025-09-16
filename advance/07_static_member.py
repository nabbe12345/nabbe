#static 원본
#heap 복사본 저장 출석부 복사본 원본 수정시 윈본으로 가야한다 그걸 바꾸는게 메서드


class Robot:
    count = 0

    def how_count(self):
        print(f'객체 메서드 : {self.count}')


    def std_count(self):
        print(f'클래스 메서드 : {self.count}')
