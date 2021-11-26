# 4948 베르트랑 공준
import math


def PrimeNumber(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n, 2*n+1):
        if i == 1:
            continue
        elif PrimeNumber(i) == True:
            cnt += 1
    print(cnt)
