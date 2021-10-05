# 6095
d = [[0 for _ in range(19)] for _ in range(19)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    d[x-1][y-1] = 1

for j in range(19):
    for k in range(19):
        print(d[j][k], end=" ")
    print()