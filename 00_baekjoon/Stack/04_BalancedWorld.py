# 4949 균형잡힌 세상

while True:
    stack = []
    flag = True
    Input = list(map(str, input()))
    if Input == ".":
        break
    for i in Input:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if not stack or stack[-1] == "(" and i == ")":
                stack.pop()
            elif not stack or stack[-1] == "[" and i == "]":
                stack.pop()
            else:
                flag = False
                break
    if flag == True:
        print("yes")
    else:
        print("no")
