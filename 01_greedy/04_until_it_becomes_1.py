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
while True:
    target = (n//k) * k # k�� ������ �������� ���� �ɶ����� -1
    count += (n-target) 
    n = target

    if n < k:
        break
    
    count += 1
    n //= k

count += (n-1)
print(count)