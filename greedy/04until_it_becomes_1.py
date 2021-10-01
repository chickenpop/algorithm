n, k = map(int, input().split())

count = 0
# while True:    
#     if(n % k == 0):
#         n //= k
#         count += 1
#         if(n == 1):
#             break
#     if(n == 1):
#         break
#     if(n % k != 0):
#         n -= 1
#         count += 1

# print(count)

#문제해설(단순)
while True:
    target = (n//k) * k # k로 나누어 떨어지는 수가 될때까지 -1
    count += (n-target) 
    n = target

    if n < k:
        break
    
    count += 1
    n //= k

count += (n-1)
print(count)