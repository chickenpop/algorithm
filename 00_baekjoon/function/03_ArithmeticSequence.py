# 1065 한수

def seq(n):
    if n < 10:
        return 1
    lst = list(map(int, str(n)))
    a = lst[0]
    d = lst[1] - a
    for j in range(len(lst)):
        if (a + d*(j)) != lst[j]:
            break
        if j == len(lst)-1:
            return 1


n = int(input())  # 1000이하의 n

cnt = 0
for i in range(1, n+1):
    if seq(i) == True:
        cnt += 1


print(cnt)
