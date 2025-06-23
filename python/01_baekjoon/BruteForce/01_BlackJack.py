# 2798 블랙잭
n, m = map(int, input().split())

n_lst = list(map(int, input().split()))
sum_save = []

for i in range(n-2):  # p, p+1, p+2의 합, 범위(n-2, n-1, n)
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if n_lst[i]+n_lst[j]+n_lst[k] <= m:  # m보다 작거나 같은 경우만 결과값 저장
                sum_save.append(n_lst[i]+n_lst[j]+n_lst[k])

sum_save.sort()
print(sum_save[-1])  # 가장 큰 값을 출력(같거나 작을수밖에 없다)
