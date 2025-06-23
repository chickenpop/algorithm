# 2178 미로 탐색
# 3장 DFS_BFS의 실전문제 미로 탈출가 완전히 같은 문제였다
from collections import deque

n, m = map(int, input().split())  # 미로 크기 n*m

maze = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    maze.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx <= -1 or ny >= m or ny <= -1:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))  # 큐에 입력을 안해서 그대로 종료되는 오류를 만듬
    return maze[n-1][m-1]


print(bfs(0, 0))
