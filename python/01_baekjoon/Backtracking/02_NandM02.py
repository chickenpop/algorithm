# 15650 N 과 M (2)

n, m = map(int, input().split())
s = []


def NnM(p):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(p, n+1):
        if i not in s:
            s.append(i)
            NnM(i+1)
            s.pop()


NnM(1)
