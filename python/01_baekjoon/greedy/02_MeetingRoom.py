#1931 회의실 배정
n = int(input())
lst = [ [0] * 2 for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    lst[i][0] = x
    lst[i][1] = y

lst.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0
for i in range(n):
    if end <= lst[i][0]:
        cnt += 1
        end = lst[i][1]

print(cnt)