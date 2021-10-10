# # 1468
# n = int(input())
# d = [[0 for _ in range(n)] for _ in range(n)]
# cnt = 0

# for i in range(n):
#     for j in range(n):
#         if i % 2 == 0:
#             cnt += 1
#             d[i][j] = cnt
#         else :
#             cnt += 1
#             d[i][n-1-j] = cnt 

# for i in d:
#     print(*i, " ")

# 1469   
# n = int(input())
# d = [[0 for _ in range(n)] for _ in range(n)]
# cnt = 0

# for i in range(n):
#     if i % 2 == 0:
#         for j in range(n-1, -1, -1):
#             cnt += 1
#             d[i][j] = cnt
#     else : 
#         for j in range(n):
#             cnt += 1
#             d[i][j] = cnt

# for i in d:
#     print(*i, " ")

# 1470 
# n = int(input())
# d = [[0 for _ in range(n)] for _ in range(n)]
# cnt = 0

# for i in range(n):
#     if i % 2 == 0:
#         for j in range(n):
#             cnt += 1
#             d[j][i] = cnt
#     else: 
#         for j in range(n-1, -1, -1):
#             cnt += 1
#             d[j][i] = cnt

# for i in d:
#     print(*i, " ")

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