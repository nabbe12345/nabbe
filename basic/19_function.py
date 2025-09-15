# 함수 선언 (define)
#선언  함수  매개변수
def toaster(bread):
    print(f'{bread}이 구워지고 있다')
    return f'구워진 {bread}'

#print , return 헷갈리지 않기        print = 우리만 보려고 찍은것  return = 밖으로 튀어나감


#함수 사용
dish = toaster('빵')
print(dish)
