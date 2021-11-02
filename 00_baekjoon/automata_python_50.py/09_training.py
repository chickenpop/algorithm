#1789 수들의 합
x = int(input())
sum = 0
cnt = 0

for i in range(x+1): # 범위 주의 range() x-1까지인데 처음에 범위를 잡아서 실패나옴
    sum += i
    if sum > x:
        cnt -= 1
        break
    cnt += 1

print(cnt)

#2753 윤년
year = int(input())

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)

# 10039 평균 점수
lst = []
sum = 0

for i in range(5):
    lst.append(int(input()))

for i in range(5):
    if lst[i] < 40:
        sum += 40
    else:
        sum += lst[i]

print(sum//5)

# 1934 최소공배수
def GCD(a, b):
    while(b):
        a, b = b, a%b
    return a

def LCM(a, b):
    result = (a*b)//GCD(a, b)
    return result

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))