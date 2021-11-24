# 1011 Fly me to the Alpha Centauri
# 시간초과, 오류 발견
import sys

TestCase = int(input())

for i in range(TestCase):
    x, y = map(int, sys.stdin.readline().split())
    move = y-x
    n = 1
    while True:
        if 2*n >= move:
            print(n+1)
            break
        else:
            n += 1