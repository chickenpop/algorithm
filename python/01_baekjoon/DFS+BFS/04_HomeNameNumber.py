# 2667 단지 번호 붙이기
from collections import deque

n = int(input())  # 정사각형 크기

block = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    block.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    block[x][y] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx <= -1 or ny >= n or ny <= -1:
                continue
            if block[nx][ny] == 0:
                continue
            if block[nx][ny] == 1:
                block[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt


cnt = []
for i in range(n):
    for j in range(n):
        if block[i][j] == 1:
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
