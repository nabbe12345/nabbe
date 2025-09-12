dic = {
    'name':'hond,go,gi',
    'phone':'12-3123-1423',
    'friends':['ho','he','ha']
}


#dic.keys() : 특정한 사전의 키들만 가져와 dict_keys 라는 객체를 반환한다
print(dic) #전부 출력
print(dic.keys()) #'key'들만 출력

for item in dic.keys():         #for ~ in ~: 만능
    print(item)
# 키만 가져온다

# dict_keys -> list 로 변환
keys = list(dic.keys())
print(keys)

# dict_keys -> tuple 로 변환
keys = tuple(dic.keys())
print(keys)


# dic.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())
# list 로 변경해서 values 라는 변수에 담아보자

for item in dic.values():
    print(item)

values = list(dic.values())
print(values)
#dic.values가 list로 변환되어 values 변수에 담긴다

#[['ho','he','ha']]는 2차원 리스트로 볼수있다


# dic.items() : 사전의 키:값 을 한 쌍으로 가져와 dict_items 로 반환한다
# 각 키와 값은 () 모양으로 보아 tuple 이다
print(dic.items())


# list로 변환해 보면 list 안에 각 키와 값이 튜플로 저장되어 있음을 알 수있다
li = list(dic.items())
print(li)


# 값을 가져오기
print(dic.get('name'))
print(dic['phone'])


# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해 보자

for it in dic.keys():
    print(it)
for ot in dic.values():
    print(ot)
#print(f'{it}:{ot}')
for item in dic.items():
    print(item)


#==========================================

#답안

# 1. 키를 뽑아낸다음 키를 가지고 값을 뽑아내는 방법

for key in dic.keys():
    print(f'{key}:{dic[key]}')         #1번째 키에서 값을 하나씩 뽑아 온다


# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방법

for item in dic.items():
    print(f'{item[0]} = {item[1]}')    #인덱스를 이용

#================================================

# 90이상인 사람의 이름만 출력
members = {
   'kim': 63, 'lee': 88, 'park': 97, "gang": 77, "hwang": 100, "ga": 65,
   "na": 92, "la": 90, "wang": 100, "gu": 79
}



win = 90
for key in members.keys():
    if members[key] >= win:
        print(f'name : {key}')



# ========================================
# 인덱스를 이용
for item in members.items():
    if item[1] >= 90:
        print(f'이름 : {item[0]}')


#============================================


# key in dic : 해당 키가 사전에 존재하는지 확인
# 검색 시작여부를 결정할수 있는 방법
ki ='kim' in members
print(f'kim은 있는가? : {ki}')

ju ='jung' in members
print(f'jung은 있는가? : {ju}')


#=================================================

# update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수

dic.update({'name':'홍길동','age':30,'married':False})
print(dic)


# dic.clear() : 사전안의 내용을 모두 지운다
dic.clear()
print(dic)
