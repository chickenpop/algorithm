# 2839 설탕 배달
n = int(input())
cnt = 0

n = int(input())
cnt = 0

while True:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    elif (n%5)%3 == 0:
        cnt += n//5 + (n%5)//3
        print(cnt)
        break
    elif (n%3)%5 == 0:
        cnt += n//3 + (n%3)//5
        print(cnt)
        break
    elif n % 3 == 0:
        cnt += n//3
        print(cnt)
        break
    elif n < 0 :
        print(-1)
        break

    n -= 3
    cnt += 1 