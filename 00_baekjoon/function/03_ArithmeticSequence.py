# 1065 한수

n = int(input())  # 1000이하의 n

cnt = 0
for i in range(1, n+1):
    if i < 10:
        cnt += 1
        continue
    lst = list(map(int, str(i)))
    a = lst[0]
    d = lst[1] - a
    for j in range(len(lst)):
        if (a + d*(j)) != lst[j]:
            break
        if j == len(lst)-1:
            cnt += 1


print(cnt)
