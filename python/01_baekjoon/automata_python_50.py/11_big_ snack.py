#4101 크냐?
while True:
    x, y = map(int, input().split())
    if x > y:
        print("Yes")
    else:
        if (x and y) == 0:
            break
        print("No")

#10156 과자
K, N, M = map(int, input().split())

if K * N > M:
    print((K*N)-M)
else:
    print(0)