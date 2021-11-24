# 2839 설탕 배달
n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    elif n < 0:
        print(-1)
    else:
        n -= 3
        cnt += 1 