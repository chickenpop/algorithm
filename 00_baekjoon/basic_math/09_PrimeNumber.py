# 1978 소수찾기 prime number
import math

def PrimeNumber(n):
    for i in range(2, int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

n = int(input()) # 소수 갯수

lst = list(map(int, input().split()))
cnt = 0
for i in range(len(lst)):
    if PrimeNumber(lst[i])== True:
        cnt += 1
    else:
        cnt += 0

print(cnt)