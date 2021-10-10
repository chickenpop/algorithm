# 1468
n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            cnt += 1
            d[i][j] = cnt
        else :
            cnt += 1
            d[i][n-1-j] = cnt 

for i in d:
    print(*i, " ")

# 1469   
n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n-1, -1, -1):
            cnt += 1
            d[i][j] = cnt
    else : 
        for j in range(n):
            cnt += 1
            d[i][j] = cnt

for i in d:
    print(*i, " ")

# 1470 
n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(n):
            cnt += 1
            d[j][i] = cnt
    else: 
        for j in range(n-1, -1, -1):
            cnt += 1
            d[j][i] = cnt

for i in d:
    print(*i, " ")

# 1471
n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    if i % 2 == 1:
        for j in range(n):
            cnt += 1
            d[j][i] = cnt
    else: 
        for j in range(n-1, -1, -1):
            cnt += 1
            d[j][i] = cnt

for i in d:
    print(*i, " ")

# 1472
n, m = map(int, input().split())
d = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

if n % 2 == 0:
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            for j in range(m):
                cnt += 1
                d[i][j] = cnt
        else :
            for j in range(m-1, -1, -1):
                cnt += 1
                d[i][j] = cnt
else :
    for i in range(n-1, -1, -1):
        if i % 2 == 1:
            for j in range(m):
                cnt += 1
                d[i][j] = cnt
        else :
            for j in range(m-1, -1, -1):
                cnt += 1
                d[i][j] = cnt


for i in d:
    print(*i, " ")

# 1473
n, m = map(int, input().split())
d = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0

for i in range(n):
    idx = n - i - 1
    if i % 2 == 0:
        for j in range(m):
            cnt += 1
            d[idx][j] = cnt
    else :
        for j in range(m-1, -1, -1):
            cnt += 1
            d[idx][j] = cnt

for i in d:
    print(*i," ")

# 1474
n, m = map(int, input().split())
d = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
k = 0

for j in range(m-1, -1, -1):
    if k % 2 == 1:
        for i in range(n):
            cnt += 1
            d[i][j] = cnt
        k += 1
    else :
        for i in range(n-1, -1, -1):
            cnt += 1
            d[i][j] = cnt
        k += 1


for i in d:
    print(*i," ")

# 1475
n, m = map(int, input().split())
d = [[0 for _ in range(m)] for _ in range(n)]
cnt = 0
k = 0

for j in range(m-1, -1, -1):
    if k % 2 == 0:
        for i in range(n):
            cnt += 1
            d[i][j] = cnt
        k += 1
    else :
        for i in range(n-1, -1, -1):
            cnt += 1
            d[i][j] = cnt
        k += 1

for i in d:
    print(*i, " ")