# 1351 구구단 출력하기 2
def times_table(num1, num2):
    for i in range(num1, num2+1):
        for j in range(1, 10):
            print(str(i)+"*"+str(j)+"="+str(i*j))

a, b = map(int, input().split())

times_table(a, b)

# 1352 사각형 출력하기 1
n = int(input())

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

# 1353 삼각형 출력하기 1
n = int(input())

for i in range(1, n+1):
    print("*"*i)

# 1354 삼각형 출력하기 2
n = int(input())

for i in range(n, 0, -1):
    print("*"*i)

# 1355 삼각형 출력하기 3
n = int(input())

for i in range(n, 0, -1):
    j = n-i
    print(" "*j+"*"*i)

# 1356 사각형 출력하기 2
n = int(input())

for i in range(n):
    if i == 0 or i == (n-1):
        for j in range(n):
            print("*", end="")
    else:
        print("*"+(n-2)*" "+"*", end=" ")
    
    print()
