# 사용방식

# from 모듈 import 함수
from oper import sum

print(f'sum() 함수 실행: {sum(5,10)}')

# import 모듈          # .은 ~ 밑에       as는 이름을 줄일수있다/별명
import oper as op
print(f'minus() 함수 실행: {op.minus(10,5)}')


