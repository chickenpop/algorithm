# # 1460
# n = int(input())

# count = 0 

# for i in range(n):
#     for j in range(n):
#         count+=1
#         print(count, end=" ")
#     print() 

# # 1461
# n = int(input())
# cnt = 0
# d = [[0 for _ in range(n)] for _ in range(n)]

# for i in range(len(d)):
#     for j in range(len(d[i]) - 1, -1, -1):
#         cnt += 1
#         d[i][j] = cnt

# for i in d:
#     print(*i, " ")

# 1462
n = int(input())
d = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        d[j][i] = cnt

for i in d:
    print(*i, " ")
