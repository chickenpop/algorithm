# 11650 좌표 정렬하기
import sys

n = int(input())
xy = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy[i][0] = x
    xy[i][1] = y

xy.sort(key=lambda x: (x[0], x[1]))  # x, y 오름차순 정렬

for i in xy:
    print(i)
