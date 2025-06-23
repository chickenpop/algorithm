# 1436 영화감독 숌

n = int(input())  # n번째 영화
number = 666  # 첫번째 종말 숫자
cnt = 0  # n번째 종말 숫자를 찾기 위한 변수

while True:
    if '666' in str(number):  # 연속되는 666 찾기
        cnt += 1
    if cnt == n:
        print(number)
        break
    else:
        number += 1  # 종말숫자 + 1
