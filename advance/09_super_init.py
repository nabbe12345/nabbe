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



# 부모 초기화가 필요 하다면 자식에게 값을 전달해서 자식이 부모에게 전달하도록 한다
class SchoolMember:     #부모

    name =''
    age  =0

    def __init__(self,name,age):                        # 3. 받아온 값으로 초기화 하고 객체화 된다.
        self.name = name
        self.age = age

class Teacher(SchoolMember):     #자식
    salary = 0

    def __init__(self,name,age,salary):
        super().__init__(name,age)                  # 2. (부모)를먼저 객체화 시키면서 초기화할 값을 전달
        self.salary = salary                        # 4. 그리고 나서 (내가) 초기화  하면서 객체화 된다.

t = Teacher('김철수',33,5000000000)
                                                    # 1.Teacher 라는 클래스를 객체화 한다.(초기화를 위해 매개변수를 전달)
print(f'{t.name}({t.age}) - {t.salary}')
                                                    # 5. name 과 age 는 부모것 이지만 내것처럼 내 객체에서 가져다 쓸 수 있게 된다.



'''
Teacher 클래스를 t 라는 변수에 객체화 시키고 매개변수에 값을 지정(초기 세팅을 위해)
이 값을 Teacher 클래스 속해있는 함수에 name age salary가 인식되고
다음 명령은 부모를 객체화 시키는 작용이 일어난다
-왜냐하면 name , age 는 부모에서 내려온 상속 변수기 때문이다-
그리고 부모 클래스(SchoolMember)에 올라가서
SchoolMember에 있는 함수에 name , age 값을 대입하고
필드 변수에 값을 같게 적용을 해준다 이유는 초기화 하고 없어지는 init 습성
그리고 print(로 아까 지정한 Teacher(클래스)가 담긴 t라는 변수를 사용하여 t.name , t.age ,t.salary 해서 값을 출력한다)
name , age 매개변수는 부모것이지만
클래스명에서 Teacher(SchoolMember)이니 Teacher는 SchoolMember에게 상속 받는 상황이다
'''
