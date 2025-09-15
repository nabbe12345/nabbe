#인자값 /parameter / 매개변수 / 레퍼런스(참조)변수          모두 같은 말
#지금은 인자값이라고 불림   함수(여기 값)


def plus(num):
    result = num + 5
    return result

print(plus(5))     # 10
print(plus()) # TypeError: plus() missing 1 required positional argument: 'num'    값을 안넣을시 에러
