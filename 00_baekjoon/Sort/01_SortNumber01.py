# 2750 수 정렬하기

n = int(input())  # n개의 수 입력
number = []

for i in range(n):
    number.append(int(input()))

number.sort()

for i in number:
    print(i)
