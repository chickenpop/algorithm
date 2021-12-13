# 팩토리얼 구현 예제, 같은 문제 baekjoon/recusion/01
# 5-5 2가지 방식으로 구현한 팩토리얼
n = int(input())


def factorial_iterative(n):  # 반복적인 구현으로 만든 팩토리얼
    result = 1
    # 1 부터 n까지의 수를 차례대로 곱하기:
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):  # 재귀적으로 구현한 팩토리얼
    if n <= 1:
        return 1
    # n != n *n(n-1)!를 코드로 작성하기
    return n * factorial_iterative(n-1)


print('반복적 구현:', factorial_iterative(n))
print('재귀적 구현:', factorial_recursive(n))
