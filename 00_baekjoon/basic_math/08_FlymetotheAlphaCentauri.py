# 1011 Fly me to the Alpha Centauri
import sys
import math
TestCase = int(sys.stdin.readline())

for i in range(TestCase):
    x, y = map(int, sys.stdin.readline().split())
    move = y-x
    if move <= 3:
        print(move)
    else: 
        n = int(math.sqrt(move))
        if n**2 == move:
            print(2*n-1)
        elif n**2 < move <= n**2+n:
            print(2*n)
        else:
            print(2*n+1)