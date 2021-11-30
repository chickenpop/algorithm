# 10870 피보나치 수 5
lst = [0, 1]

n = int(input())  # n 번째 피보나치 수

lst = [0, 1]

if n < 2:
    print(lst[n])
else:
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])

    print(lst[-1])
