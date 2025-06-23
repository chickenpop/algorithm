# 1402
n = int(input())
d = [0 for _ in range(n)]

d = map(int, input().split())

data = sorted(d, reverse=True)

for i in range(n):
    print(data[i], end=" ")

# 1403
n = int(input())
d = [0 for _ in range(n)]

d = list(map(int, input().split()))
cnt = 0

for i in range(2):
    for j in range(n):
        print(d[j])

# 1405
n = int(input())
d = [0 for _ in range(n)]
k = 0
d = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        print(d[i+j-n], end=" ")
    print()

# 1407
d = list(map(str, input().strip().split()))

for i in range(len(d)):
    print(d[i], end="")

# 1409
d = list(map(int, input().split()))
k = int(input())

print(d[k-1])

# 1410 올바른 괄호 1 (괄호 개수 세기)
d = str(input())
left = 0
right = 0

for i in range(len(d)):
    if d[i] == "(":
        left += 1
    elif d[i] == ")":
        right += 1

print(left, right)