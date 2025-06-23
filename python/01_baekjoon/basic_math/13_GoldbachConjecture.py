# 9020 골드바흐의 추측
import math


def PrimeNumber(num):  # 2이상의 소수 판별 함수
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num)+1)):
            if num % i == 0:
                return False
        return True


TestCase = int(input())  # n 테스트 케이스 수

for i in range(TestCase):
    n = int(input())
    q = int(n/2)  # n의 절반
    p = int(n/2)  # n의 절반
    while True:  # n의 절반값을 하나는 올리고 낮추면서 둘다 소수면 출력
        if PrimeNumber(q) == True and PrimeNumber(p):
            print(q, p)
            break
        else:
            q -= 1
            p += 1
