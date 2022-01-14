# 10828 스택

stack = []  # 스택
n = int(input())  # 스택 명령 총 횟수

for i in range(n):
    order = input().split()

    if order[0] == 'push':  # 스택에 정수를 넣는다.
        stack.append(order[1])
    elif order[0] == 'pop':  # 스택에서 가장 위에 있는 정수 뺀다. 없으면 -1
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':  # 스택의 정수 갯수
        print(len(stack))
    elif order[0] == 'empty':  # 스택이 비어 있으면 1, 아니면 0
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':  # 가장 위에 있는 정수 출력, 정수 없으면 -1
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
