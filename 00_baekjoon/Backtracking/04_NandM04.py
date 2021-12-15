# 15652 N과 M (4)

n, m = map(int, input().split())

lst = []


def NnM4(k):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(k, n+1):
        lst.append(i)
        NnM4(i)
        lst.pop()


NnM4(1)
