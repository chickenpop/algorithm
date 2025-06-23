# 1929 소수 구하기
import math


def PrimeNumber(num):  # 2 이상의 소수 판별 함수
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


m, n = map(int, input().split())
lst = []  # 소수 저장
for i in range(m, n+1):  # m~n까지의 소수 저장 반복문
    if i == 1:  # 1의 소수가 아니고 함수에 적용이 안되서 넘긴다
        continue
    elif PrimeNumber(i) == True:
        lst.append(i)

for i in range(len(lst)):
    print(lst[i])
