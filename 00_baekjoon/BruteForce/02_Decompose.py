# 2231 분해합

n = str(input())  # 어떤 자연수, 1 <= N <= 1,000,000


def decompose(num):
    sum = int(num)
    for i in range(len(num)):
        sum += int(num[i])
    return sum


print(decompose(n))
