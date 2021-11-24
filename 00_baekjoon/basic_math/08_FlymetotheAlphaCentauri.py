# 1011 Fly me to the Alpha Centauri
import sys

TestCase = int(input())

for i in range(TestCase):
    x, y = map(int, sys.stdin.readline().split())
    move = y-x-1
    i = 1
    cnt = 1
    while move != 0:
        if move >= i:
            move -= i
            i += 1
            cnt += 1
        else:
            i -= 1
    print(cnt)