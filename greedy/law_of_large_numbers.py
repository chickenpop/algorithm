N, M, K = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
frist = array[N-1]
second = array[N-2]
count = 0

while True:
    for i in range(K):
        if(M == 0):
            break
        count += frist
        M-=1
    if(M == 0):
        break
    count += second
    M-=1
    
print(count)