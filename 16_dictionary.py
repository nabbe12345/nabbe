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
a = {'first':'a'}        # a 사전에 키 : 값을 넣었다
print(a)

# 사전에 데이터 넣기 2
a['second'] = 'b'
print(a)

#사전에서 특정 요소 삭제
del a['second']
print(a)

#사전의 특정 요소를 꺼내보자(사용법은 List 와 비슷하다)
print(dic2['name'])
print(dic2['friends'])

#get 메서드를 활용해서도 가져올 수 있다
print(dic2.get('phone'))
print(dic2.get('nick','해당 내용이 없음'))
#특정 키가 없는 경우 none이 아닌 대체 내용으로 반환 할수있음




