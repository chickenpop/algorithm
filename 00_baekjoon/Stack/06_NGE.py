# 17298 오큰수

n = int(input())  # 수열의 크기
stack = []
stack = list(map(int, input().split()))
stack.append(-1)  # -1 출력용

for i in range(n):
    Nge = stack[i]
    for j in range(i+1, n+1):
        if Nge < stack[j]:
            print(stack[j], end=" ")
            break
        elif j == n:
            print(stack[j], end=" ")  # -1 출력
