# 11650 좌표 정렬하기
import sys

n = int(input())
xy = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy.append([x, y])  # 2차원 리스트 넣기

xy.sort(key=lambda x: (x[0], x[1]))  # x, y 오름차순 정렬

for i in range(n):
    print(xy[i][0], xy[i][1])
