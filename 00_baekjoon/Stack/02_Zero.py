# 10773 제로
stack = []

k = int(input())  # k개의 정수

for i in range(k):
    order = int(input())
    if order == 0:  # 0이면 pop()
        stack.pop()
    else:  # 아니면 push
        stack.append(order)

print(sum(stack))
