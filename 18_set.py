# set 은 순서가 없고 중복을 허용하지 않는다
number_set = set([1,2,3,4,5,6])
print(number_set)


str_set = set('HelloWorld')          # 중복을 제외하고 담는다 ex) L 3개  o 2개
print(str_set)                       # 그래서 중복 제거용도로 사용된다




# set 들을 이용해서 집합을 구현할 수 있다
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])


# 교집합(intersection) 교차하는것
print(f'교집합1 : {s1 & s2}')             #  and(&)로 표현
print(f'교집합2 : {s1.intersection(s2)}') # .intersection() 으로도 표현 가능

# 합집합(union) 더하는것
print(f'합집합1 : {s1 | s2}')             # or(|)로 표현 중복은 안가져오고 한쪽에서만 가져옴
print(f'합집합2 : {s1.union(s2)}')        # .union() 으로도 표현 가능

# 차집합(minus|difference)     얼마나 차이나?     ex)단차
print(f'차집합1 : {s1-s2}')               # -로 표현
print(f'차집합2 : {s2-s1}')      # set은 작업 하다보면 순서가 바뀐다


#======================================================



s1.add(10) # 값 1개 추가하기 .add()
print(s1)

# 여러개 추가하기 .update() 중복은 X
s1.update([10,20,30])
print(s1)

# 특정값 제거  KeyError: 10 키에 10
s1.remove(10)
print(s1)
# s1.remove(10) <- 없는 값을 지우려고 하면 KeyError 발생
s1.discard(10) # remove 와 같으나 없는 값을 지우려고 해도 에러가 나지 않는다


