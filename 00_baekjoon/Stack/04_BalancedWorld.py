# 4949 균형잡힌 세상
import sys

while True:
    stack = []
    flag = True
    Input = list(map(str, sys.stdin.readline()))
    if Input == ".":
        break
    for i in Input:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    if flag == True:
        print("yes")
    else:
        print("no")
