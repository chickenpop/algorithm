# 2581 소수
import math

def PrimeNumber(num):
    if num < 3:
        return (2 if num == 2 else 0) 
    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return 0 # 소수면 0을 반환
        return num # 소수면 그대로 반환

m = int(input())
n = int(input())
lst = [0]
for i in range(m, n+1):
    if PrimeNumber(i) != 0: # 반환값이 0이 아니면 lst에 저장
        lst.append(PrimeNumber(i))

if sum(lst)==0: # 0 이면 소수가 없어서 -1
    print(-1)
else: # 0 이상이면 소수가 존재해서 합과 최솟값
    print(sum(lst))
    print(lst[1])