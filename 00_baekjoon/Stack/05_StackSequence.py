# 1874 스택 수열

stack = []
n = int(input())
n_stack = [i for i in range(n, 0, -1)]
print(n_stack)
for i in range(n):
    Input = int(input())
    for i in range(len(n_stack)):
        if i == Input:
            n_stack.pop()
            break
        elif i in n_stack:
            stack.append(i)
    print(stack)
