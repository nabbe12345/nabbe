class Puppy:
#Puppy 맴버는 name,goal< 변수 init이라는 생성자

    name='' #멤버 변수(필드) : class 안에서 사용 가능한 변수
    goal=''                                       #4

    def __init__(self,name,goal):                 #1
        # 생성자 : 초기화를 하는것 객체화시 호출되는 '함수'
        # 클래스 변수 name,goal를 초기화
        #self = 나를 의미함
        self.name=name                            #3
        self.goal=goal

puppy = Puppy('멍멍이','집지키기')         #2
print(f'이름 : {puppy.name} / 목적: {puppy.goal}')






#==================================================================


#생성자: 객채(복사)가 생성되면서 필요한 값을 초기화(세팅)하는것   단 쓰임이 다하면 사라진다
#Puppy 객체를 초기화(세팅) 하는 조건 / 이름과 목적을 세팅해준다
#세팅 해준 값을 puppy 라는 변수에 담아준다
#init에 name , goal 값이 멍멍이 , 집지키기로 설정이 되었으나
#생성자는 쓰임이 다하면 사라지기 때문에 (멍멍이,집지키기라는 값)
#name , goal을 멤버 변수로 지정을 해줘야한다
#멤버 변수로 지정을 해주는 과정에 어떤것이 객체의 멤버인지 알수없다 (일련번호가 다름)
#그래서 self 라는것으로 self.name = name(생성자 세팅)을 같게 만든다


#==============================================================



#   def __init__(self, name, goal):
#   puppy = Puppy('멍멍이', '집지키기')
#   self.name = name
#   self.goal = goal
#   name=''
#   goal=''


#      받아온 name 과 goal 은 이 생성자를 벗어날수 없다.(생성자의 쓰임이 다하면 함께 없어진다.)
#                             / def 문장에서만 사용가능 /
#                          def __init__(self, name, goal):


#        그래서 클래스(객체) 멤버 에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능 하다.
#                     / 메인 클래스 창에 변수를 만들어야 하는 이유/
#                         puppy = Puppy('멍멍이', '집지키기')


#           그런데  name = name 형태로는 어떤것이 객체의 멤버인지 알 수 없다.
#                        / 일련번호가 다르고 구분이 어려움 /
#                                    name=name
#                                    goal=goal

#                  그래서 멤버인 녀석은 self 를 이용하여 표시해 준다
#                    / self로 클래스 멤버와 함수와 같게 설정한다 /
#                    / 이유는 한 생성자의 쓰임이 다하면 없어지는 이유 /
#                               self.name = name
#                               self.goal = goal
