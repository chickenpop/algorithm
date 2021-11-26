# 1978 소수찾기 prime number
import math

def PrimeNumber(n):
    # 예외 사항 if n==1, n==2
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:      # 2~제곱근까지의 수가 n(입력)과 나눠지면 소수가 아니다
                return False
    return True             # 소수

n = int(input()) # 소수 갯수

lst = list(map(int, input().split()))
cnt = 0
for i in range(len(lst)):
    if PrimeNumber(lst[i]) == True:
        cnt += 1
    else:
        cnt += 0

print(cnt)