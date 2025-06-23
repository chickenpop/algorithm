# 1874 스택 수열
import sys

n = int(sys.stdin.readline())
stack = []
start = 1
result = []
flag = True
for i in range(n):
    Input = int(sys.stdin.readline())
    while start <= Input:
        stack.append(start)
        result.append("+")
        start += 1

    if stack[-1] == Input:
        stack.pop()
        result.append("-")
    else:
        flag = False
        print("NO")
        break
    if flag == False:
        break

if flag == True:
    for i in result:
        print(i)
