# 10872 팩토리얼

import math


def Factorial(num):  # 팩토리얼 재귀 함수 n * n-1(함수 실행)
    return num * Factorial(num-1) if num > 1 else 1


n = int(input())

print(Factorial(n))

# 다른 팩토리얼 구하는 방법 1 반복문 2 math 함수
result = 1
for i in range(1, n+1):
    result *= i

print("반복문을 이용한 팩토리얼: %d" % result)


print("math함수 팩토리얼: %d" % math.factorial(n))
