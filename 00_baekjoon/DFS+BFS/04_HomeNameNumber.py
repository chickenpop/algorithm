# 2667 단지 번호 붙이기
from collections import deque

n = int(input())  # 정사각형 크기

block = []
visited = [[0]*(n) for _ in range(n)]

for i in range(n):
    block.append(list(map(int, input())))


def dfs(x, y):
    if x >= n or x <= -1 or y >= n or y <= -1:
        return
    if block[x][y] == 1:
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)


dfs(0, 0)

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1

print(cnt)
