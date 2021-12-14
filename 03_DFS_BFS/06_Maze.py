# 실전 문제 미로 탈출
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):  # 네 방향 전부 조사
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if maze[nx][ny] == 0:  # 괴물 존재
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 이동 거리마다 1, 2, 3... 추가됨
                queue.append((nx, ny))
    return maze[n-1][m-1]


n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))  # 시작 위치 (1, 1)
