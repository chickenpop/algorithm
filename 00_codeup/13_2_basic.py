# 6084
hz, bit, c, s = map(int, input().split())
result = (hz*bit*c*s)/(8*1024*1024)

print("{:.1f} MB".format(result)) # �Ҽ��� 2��°���� �ݿø�

# 6085
w, h, b = map(int, input().split())
result = (w*h*b)/(8*1024*1024)

print("{:.2f} MB".format(result))

# 6086 
n = int(input())
sum = 0

for i in range(n+1):
    sum += i
    if n <= sum:
        print(sum)
        break

# 6087
n = int(input())

for i in range(n+1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

# 6088
a, d, n = map(int, input().split())

print(a+(d*(n-1)))

# 6089
a, r, n = map(int, input().split())

print(a*(r**(n-1)))

6090
a, r, d, n = map(int, input().split())

for i in range(n-1):
    a *= r
    a += d

print(a)

# 6091  #최대공약수, 최소 공배수
def gcd(x, y):
    while y :
        x, y = y, x % y
    return x

def lcm(x, y):
    return x*y // gcd(x, y)

day1, day2, day3 = map(int, input().split())

result = lcm(day1, day2)
result = lcm(result, day3)
print(result)