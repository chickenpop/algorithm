# 1260 DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())  # 정점, 간선, 탐색 시작번호

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort()


dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, dfs_visited)
print()
bfs(graph, v, bfs_visited)
