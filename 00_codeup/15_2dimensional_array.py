# 6095
# d = [[0 for _ in range(19)] for _ in range(19)]

# n = int(input())

# for i in range(n):
#     x, y = map(int, input().split())
#     d[x-1][y-1] = 1

# for j in range(19):
#     for k in range(19):
#         print(d[j][k], end=" ")
#     print()

# 6096
# d = [[0 for _ in range(19)] for _ in range(19)]

# for l in range(19):
#     d[l] = list(map(int, input().split()))

# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     for j in range(19):
#         if d[j][y-1] == 1:
#             d[j][y-1] = 0
#         else : d[j][y-1] = 1
        
#         if d[x-1][j] == 1:
#             d[x-1][j] = 0
#         else : d[x-1][j] = 1


# for l in range(19):
#     for k in range(19):
#         print(d[l][k], end=" ")
#     print()