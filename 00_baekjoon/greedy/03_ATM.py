#11399 ATM
n = int(input())
lst = []
lst = list(map(int, input().split()))

lst.sort()

sum_lst = []
sum = 0
for i in range(n):
    sum = lst[i] + sum
    sum_lst.append(sum)

sum = 0
for i in range(len(lst)):
    sum += sum_lst[i]

print(sum)