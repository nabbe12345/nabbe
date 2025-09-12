#리스트 번호가 붙어있는 순서대로       방번호로 구분
#dictionary '사전'  key:값     중복x  문자열로 구분
from tkinter.font import names

# 사전은   키:값  형태로 되어있다

# 비슷한 자료구조로는
# 자바스크립트: 오브젝트
# 자바: 맵

# 사용 기호             [] list     () tuple    {} dictionary


dic1 = {
    'name':'joe_jang_woo',
    'phone':'010-9776-9603',
    'age':30
}

dic2 ={
    'name':'hello',
    'phone':'123',
    'friends':['hi','bye','hey']  #리스트 활용
}

# 사전에 데이터 넣기 1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

#사전에서 특정 요소 삭제
del a['second']
print(a)






