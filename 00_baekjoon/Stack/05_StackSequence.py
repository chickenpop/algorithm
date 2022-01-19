# 1874 스택 수열
import sys
stack = []
n = int(sys.stdin.readline())
flag = True
start = 1
for i in range(n):
    Input = int(sys.stdin.readline())
    for i in range(start, n+2):
        if i == Input and stack and i == stack[-1]:
            stack.pop()
            print("-")
            start = i
            break
        elif Input in stack and stack[-1] == Input:
            stack.pop()
            print("-")
            start = i
            break
        elif Input in stack and stack[-1] != Input:
            print("NO")
            flag = False
            break
        else:
            stack.append(i)
            print("+")
    if flag == False:
        break
