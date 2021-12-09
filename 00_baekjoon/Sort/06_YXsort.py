# 11651 좌표 정렬하기 2
import sys

n = int(input())
Yx = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    Yx.append([x, y])

Yx.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(Yx[i][0], Yx[i][1])
