# 15651 N 과 M (3)

n, m = map(int, input().split())

lst = []


def dfs():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return True

    for i in range(1, n+1):
        lst.append(i)
        dfs()
        lst.pop()


dfs()
