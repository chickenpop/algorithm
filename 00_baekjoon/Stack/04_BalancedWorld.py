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
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        else:
            flag == False
            break
    if flag == True:
        print("yes")
    else:
        print("no")
