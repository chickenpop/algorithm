# 4948 베르트랑 공준
import math
import sys


def PrimeNumber(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True


all_lst = list(range(2, 246912))  # 지정 범위만큼 리스트 생성
save_lst = []

for i in all_lst:
    if PrimeNumber(i) == True:
        save_lst.append(i)

n = int(sys.stdin.readline())

while n != 0:
    cnt = 0
    for i in save_lst:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
    n = int(sys.stdin.readline())
