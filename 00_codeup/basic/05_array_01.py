# 1402
n = int(input())
d = [0 for _ in range(n)]

d = map(int, input().split())

data = sorted(d, reverse=True)

for i in range(n):
    print(data[i], end=" ")