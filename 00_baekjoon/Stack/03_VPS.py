# 9012 괄호

n = int(input())  # 테스트 케이스 수
for i in range(n):
    stack = []
    vps = list(map(str, input()))
    for i in range(len(vps)):
        if vps[i] == "(":
            stack.append(1)
        else:
            stack.append(-1)
    if sum(stack) == 0:
        print("YES")
    else:
        print("NO")
    print(stack)
