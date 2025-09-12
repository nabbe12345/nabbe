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



