'''
데이터 프레임은 엑셀형태로 변환된 데이터 형태
2차원
DateFrame은 함수가 아니라 class
행과 열이 있는 표 형태 (엑셀 형태)
열(column)은 서로 다른 데이터 타입을 가질 수 있다
열 = column 행 = row

키 = column name , 값 = row


==============
print(df.loc[index]) 출력시 가져오는 형태는 series 형태로 불러온다
시리즈에서는 컬럼명을 같이 표시한다
단 컬럼명이 없을시 자동으로 0부터 ~ 숫자를 붙인다

                'loc[n]은 n번째 row 를 가져온다'

print(df.loc[[1,2]]) 1 ,2 번 index row 값 가져오기
print(df.loc[1:7])  슬라이싱/ 1 부터 7 까지 row값 가져오기
                    *주의* DateFrame 에서만 !     1:6 XX



date = {
    'calories':[1003,10004,1005],
    'duration':[50,60,70],
    'score':[1,2,3]
}

df = pd.DataFrame(date, index=['D1', 'D2', 'D3'])   DateFrame 인덱스에 이름 주기

    calories  duration  score
D1      1003        50      1
D2     10004        60      2
D3      1005        70      3

===================================
print(df.columns)   컬럼이 뭐뭐 있는지 전부 알려줌

yoyo = 'calories' in df.columns    특정 컬럼이 있는지 확인법
print(yoyo)


컬럼 값들 불러오기

print(df['column']) column 에 컬럼을 넣어 값을 불러온다

print(df[df.columns.difference(['column'])])  <- [제외 시킬 컬럼 여러개 가능] 리스트형식

=========================================

df.columns = ['칼로리','시간','점수'] <- 전체 컬럼을 바꾸는것 갯수가 동일해야만 가능
 '특정 컬럼만 바꾸면 에러'


new_df = df.rename(columns={'시간':'time'} <- 특정 컬럼만 이름을 바꾸는것
.rename 으로 컬럼의 특정 이름 변경하고 반환된 df를 new_df에 담아는다
복사본이니 원본에서는 변화가 없다
'{}는 dic(사전) 형식이니  키와 값이 있다'
key = 현 컬럼 이름  val = 변경 하려는 컬럼 이름


dp.drop(['삭제하고 싶은 index']) 특정 row 삭제하기
new_df = df.drop(['D3','D2'])  [] 리스트로 감싸서 여러개 삭제 가능


df.drop(['삭제하고싶은 컬럼'], axis=1) 특정 컬럼 삭제하기
axis는 축 / 0은 가로 1은 세로

pandas 에서 remove를 사용하지 않고 drop 을 사용하는 이유
pandas 에서 더 효율적이고 axis 라는 기능으로 쉽게 제거가능
그리고 대표적인 차이는 remove는 list에서 값을 지울때 사용
ex) a = [1,2,3,4]
remove(3)
3이 사라짐

pandas 데이터전처리를 하는 라이브러리

'''