# # 1172
# num = list(map(int, input().split()))

# num.sort()

# print(*num, sep=" ")

# # 1420
# n = int(input())
# d = {}

# for i in range(n):
#     name, score = input().split()
#     d[name] = int(score)

# data = sorted(d.items(), key= lambda t:t[1], reverse=True)

# print(data[2][0])

''' 
문제의 해결방향과 다른 풀이 방법
밑에 경우는 오름차순 정렬에 관련된 방법

# 1441 
n = int(input())
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = int(input())
    
d.sort()

for i in range(n):
    print(d[i])

# 1442
n = int(input())
d = [0 for _ in range(n)]
data = []

for i in range(n):
    d[i] = int(input())
    
data = sorted(d, reverse = False)

for i in range(n):
    print(data[i])

'''

# 3011
n = int(input())
d = list(map(int, input().strip().split()))
cnt = 0

for i in range(n):
    swapped = False
    for j in range(n-i-1):
        if(d[j] > d[j+1]):
            d[j], d[j+1] = d[j+1], d[j]
            swapped = True
    if swapped:
        cnt+=1

print(cnt)