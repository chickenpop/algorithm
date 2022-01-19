# 1874 스택 수열
import sys

n = int(sys.stdin.readline())
stack = []
start = 1
for i in range(n):
    Input = int(sys.stdin.readline())
    while start <= Input:
        stack.append(start)
        print("+")
        start += 1

    if stack[-1] == Input:
        stack.pop()
        print("-")
    elif len(stack) == 0:
        break
    else:
        print("NO")
        break
