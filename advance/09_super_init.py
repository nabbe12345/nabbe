# 객체화시 내 자신에서 부모를 먼저 객체화 하고 그리고 내가 객체화 된다

class Parent():
    def __init__(self):
        print('부모 생성자 실행!@#!@#')


class Child(Parent):
    def __init__(self):
        super().__init__()  # 생략된 부모 생성자
        # super()는 부모를 뜻함
        #자식이 부모생성자를 먼저 부름
        print('자식 생성자')




ch = Child()



# 부모가 초기화가 필요 하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다
class SchoolMember:     #부모

    name =''
    age  =0

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Teacher(SchoolMember):     #자식
    salary = 0

    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

t = Teacher('김철수',33,5000000000)
print(f'{t.name}({t.age}) - {t.salary}')
