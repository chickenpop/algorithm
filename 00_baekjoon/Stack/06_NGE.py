# 17298 오큰수
import sys
n = int(sys.stdin.readline())  # 수열의 크기
stack = []
stack = list(map(int, sys.stdin.readline().split()))
stack.append(-1)  # -1
result = []

for i in range(n):
    Nge = stack[i]
    for j in range(i+1, n+1):
        if Nge < stack[j]:
            result.append(stack[j])
            break
        elif j == n:
            result.append(stack[j])  # -1 출력

for i in result:
    print(i, end=" ")
