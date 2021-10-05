# 6092
n = int(input())
num = list(map(int, input().split()))
d = []

for i in range(23):
    d.append(0) 

for j in range(n):
    d[num[j]-1] += 1

for k in range(23):
    print(d[k], end=" ")