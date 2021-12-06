# 1436 영화감독 숌

n = int(input())  # n번째 영화
number = 666
number_str = '666'
cnt = 0

while True:
    for i in range(len(number_str)-2):
        if number_str[i] == '6' and number_str[i+1] == '6' and number_str[i+2] == '6':
            cnt += 1

    if cnt == n:
        print(number_str)
        break
    else:
        number += 1
        number_str = str(number)
