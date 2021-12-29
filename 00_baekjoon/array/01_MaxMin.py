# 10818 최소, 최대

n = int(input())

lst = list(map(int, input().split()))

print(min(lst), max(lst))

# 시간초과
n = int(input())

lst = list(map(int, input().split()))

for i in range(n):
    index = i
    for i in range(len(lst)):
        if lst[index] > lst[i]:
            lst[index], lst[i] = lst[i], lst[index]

print(lst[-1], lst[0])
