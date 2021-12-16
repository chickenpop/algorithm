# 1260 DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())  # 정점, 간선, 탐색 시작번호

graph = []

for i in range(m):
    x, y = map(int, input().split())
    graph.append([x, y])

# 아 기본부터 연습해야겠어... 벌써 구조가 기억이 안남
