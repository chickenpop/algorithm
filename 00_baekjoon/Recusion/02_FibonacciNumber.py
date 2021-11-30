# 10870 피보나치 수 5
lst = [0, 1]


def Fibonacci(num, cnt):  # 1번째부터 적용가능한 피보나치 함수
    cnt += 1
    lst.append(lst[cnt-1] + lst[cnt-2])  # Fn = Fn-1 + Fn-2
    return Fibonacci(num - 1, cnt) if num > 2 else lst[-1]


n = int(input())  # n 번째 피보나치 수

if n == 0:
    print(0)
else:
    print(Fibonacci(n, 1))
