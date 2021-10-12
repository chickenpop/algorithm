# # 1172
# num = list(map(int, input().split()))

# num.sort()

# print(*num, sep=" ")

# 1420
# n = int(input())
# d = {}

# for i in range(n):
#     name, score = input().split()
#     d[name] = int(score)

# data = sorted(d.items(), key= lambda t:t[1], reverse=True)

# print(data[2][0])

# 1441
n = int(input())
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = int(input())
    
d.sort()

for i in range(n):
    print(d[i])