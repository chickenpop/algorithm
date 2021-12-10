# 10989 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
number = []

for i in range(n):
    number.append(sys.stdin.readline().rstrip())

number.sort()

for i in number:
    print(i)
