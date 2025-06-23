# 4949 균형잡힌 세상
import sys

while True:
    stack = []
    flag = True
    Input = sys.stdin.readline().rstrip()
    if Input == ".":
        break
    for i in Input:
        if i == "(" or i == "[":  # 열린 기호 push
            stack.append(i)
        elif i == ")":  # 기호 일치하면 pop
            if stack and stack[-1] == "(":
                stack.pop()
            else:  # 기호 불일치 break
                flag = False
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                flag = False
                break
    if flag == True and not stack:  # 스택도 비어 있어야한다
        print("yes")
    else:
        print("no")
