# 17298 오큰수
import sys
n = int(sys.stdin.readline())  # 수열의 크기
stack = []
result = [-1] * n
stk = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    while stack and stk[stack[-1]] < stk[i]:
        result[stack[-1]] = stk[i]
        stack.pop()
    stack.append(i)

print(*result)
