# 1251 1~100까지 출력
for i in range(100):
    print(i+1, end=" ")

# 1252 1~n까지 출력
n = int(input())

for i in range(n):
    print(i+1, end=" ")

# 1253 a부터 b까지 출력
a, b = map(int, input().split())
max = 0 
min = 0

if a < b :
    max = b
    min = a
else : 
    max = a
    min = b

for i in range(min-1, max):
    print(i+1, end=" ")

# 1254 알파벳 출력하기
first, last = input().split()

for i in range(ord(first), ord(last)+1):
    print(chr(i), end=" ")

# 1255 두 실수 사이 출력하기
a, b = map(float, input().split())

while a <= b:
    print("%.2f" % a, end=" ")
    a += 0.01

# 1256 별 출력하기
n = int(input())
for i in range(n): print("*", end="")

# 1257 두 수 사이의 홀수 출력하기
a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 2 == 1:
        print(i, end=" ")

# 1258 1부터 n까지 합 구하기
n = int(input())
sum = 0

for i in range(n):
    sum += i+1

print(sum)

# 1259 1~n까지 중 짝수의 합 구하기
n = int(input())
sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum += i

print(sum)

# # 1260 3의 배수의 합
a, b = map(int, input().split())
sum = 0
for i in range(a, b+1):
    if i % 3 == 0:
        sum += i

print(sum)