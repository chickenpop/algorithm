# 2606 바이러스

computer_num = int(input())  # 컴퓨터 수
network_com = int(input())  # 네트워크와 연결되어 있는 컴

computer = [[]*computer_num for i in range(computer_num+1)]

for i in range(network_com):
    x, y = map(int, input().split())
    computer[x].append(y)
    computer[y].append(x)

com_visited = [False] * (computer_num+1)
cnt = 0


def dfs(computer, i, visited):
    visited[i] = True
    global cnt
    for j in computer[i]:
        if not visited[j]:
            cnt += 1
            dfs(computer, j, visited)


dfs(computer, 1, com_visited)

print(cnt)
