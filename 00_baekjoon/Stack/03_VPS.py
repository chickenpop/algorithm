# 9012 괄호

stack = []
n = int(input())  # 테스트 케이스 수
for i in range(n):
    vps = list(map(str, input()))
    right = 0
    left = 0
    for i in range(len(vps)):
        if vps[i] == "(":
            left += 1
        else:
            right += 1
    if right == left:
        print("YES")
    else:
        print("NO")
