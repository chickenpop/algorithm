# 15652 N과 M (4)

n, m = map(int, input().split())

lst = []


def NnM4():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(1, n+1):
        if sum(lst) <= i:
            lst.append(i)
            NnM4()
            lst.pop()


NnM4()
