# 10828 스택

stack = []  # 스택
order = []  # 명령저장
n = int(input())  # 스택 명령 총 횟수

for i in range(n):
    index = 0
    order.append(input().split())
    if order[index][0] == 'push':
        stack.append(order[i][1])
        index += 1
    elif order[index][0] == 'pop':
        if len(order) > 0:
            stack.pop()
        else:
            print(-1)
        if index != 0:
            index -= 1
    elif order[index][0] == 'size':
        print(len(order))
        index += 1
    elif order[index][0] == 'empty':
        if len(order) == 0:
            print(1)
            index += 1
        else:
            print(0)
            index += 1
    else:
        print(-1)
