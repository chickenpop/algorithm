# 10870 피보나치 수 5

def Fibonacci(num):
    return num + Fibonacci(num-1) if num > 0 else num


n = int(input())  # n 번째 피보나치 수

print(Fibonacci(n))
