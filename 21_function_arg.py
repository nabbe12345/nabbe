#인자값 /parameter / 매개변수 / 레퍼런스(참조)변수          모두 같은 말
#지금은 인자값이라고 불림   함수(여기 값)

# 인자값으로 아무것도 들어오지 않았을 경우 에러를 방지하기 위해 기본값 설정이 가능


def plus(num = 0):
    # plus(num = 0 ) 에러가 안뜨고 처리할수있게 하기 위해 기본값 넣기
    result = num + 5
    return result

print(plus(5))     # 10

print(plus()) # TypeError: plus() missing 1 required positional argument: 'num'    
# 값을 안넣을시 에러

