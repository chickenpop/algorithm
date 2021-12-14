# 실전 문제 음료수 얼려 먹기

n, m = map(int, input().split())  # 얼음 틀 크기 n*m
ice = []
for i in range(n):
    ice.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:  # 경로 외 조건
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1  # 방문처리
        # 좌우하상, 근접한 경로도 방문처리
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:  # 첫방문에만 +1, 재귀로 인해 방문처리는 카운트되지 않음
            cnt += 1

print(cnt)
