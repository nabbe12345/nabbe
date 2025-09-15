# 문자열을    ' or " (싱글,더블) 모두 사용가능
name ="joe jang-woo"
content = "My Content"

# 여러줄의 문자열을 변수에 담을때 ''' 3번 '''   or """ 3번 """
multi = '''this is multi line striong
this is second line'''


print('name:'+name) # 문자 + 문자라 f가 안들어간다
print('content:'+content)
print('multi:'+multi)

#======================================================

# 문자열에 다른 타입의 데이터를 함께 출력할 경우
age = 33

print('1 내 이름은 {0}이고 나이는 {1} 입니다'.format(name,age))
#.format( 0 , 1 )

print('1-1 내 나이는 {0}이고 이름은 {1} 입니다'.format(age,name))
print('2 내이름은' +name+'이고 나이는'+str(age)+'입니다')
#정수라 기본age는 사용 불가 // str(string)함수를 추가해 문자열로 변환
print(f'3 내이름은 {name} 이고 나이는 {age} 입니다')
#f를 이용한 방식


#========================================================


#여러줄 -> 한줄 처리 , 한줄 -> 여러줄처럼 줄바꿈

print('이것은 한줄이지만\n여러줄처럼 보이게 할겁니다')  # \n = new line 줄바꿈
print('이것은 두줄이지만\
한줄처럼 보이게 할겁니다')  # \ 한줄 처럼 보이게 하는것











