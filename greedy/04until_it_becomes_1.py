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

#�����ؼ�(�ܼ�)
while n >= k:
    while n % k != 0:
        n-=1
        count += 1
    n // k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count) 