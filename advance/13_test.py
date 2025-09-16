#
# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다')
# except Exception:
#     text = input('값을 넣으면 문자로 변환 됩니다')
#     str = str(text)
#     print(f'당신이 입력한 값 : {str} 이 문자로 변환 되었습니다')
#
# finally:
#     print('  ----------------------------------끝----------------------  ')

'''
1 try로 기존 코드 묶기
2 문자열을 넣었을시 나오는 오류를 except Exception 으로 예외를 두기
3 입력값을 문자로 바꿔 출력하기

3 마지막 출력하기'''


# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다')
# except Exception:
#     print('숫자만 가능합니다')
# finally:
#     print('그거는 문자입니다')



# text = ''
# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다')
# except Exception:
#     str = str(text)
#     print(f'당신이 입력한 값 : {str} 이 문자로 변환 되었습니다')
#
# finally:
#     print('  ----------------------------------끝----------------------  ')

#
# go = input(int)
#
# while True:
#  try:
#     text = input('값을 넣으면 숫자로 변환 됩니다')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다')
#  except Exception:
#     print(f'입력하신 값은 숫자가 아닙니다 다시 입력하세요')
#     if go == num:
#         break
#     else:
#        return
#
#  finally:
#      print(' -------------------- 끝 ------------------')





while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다')
        num = int(text) #문제가 발생
        print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다')
        break
    except ValueError: #여기로 이동
        print(f'{text} 는 숫자가 아닙니다')









