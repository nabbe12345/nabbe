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

