# 객체화시 내 자신에서 부모를 먼저 객체화 하고 그리고 내가 객체화 된다

class Parent():
    def __init__(self):
        print('부모 생성자 실행!@#!@#')


class Child(Parent):
    def __init__(self):
        super().__init__()  # 생략된 부모 생성자
        print('자식 생성자')




ch = Child()
