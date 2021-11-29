# 1002 터렛
import math

TestCase = int(input())

for i in range(TestCase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 조규현과 백승환 사이의 거리

    if r1 == r2 and distance == 0:
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance:
        print(1)
    elif abs(r1-r2) < distance < r1+r2:
        print(2)
    else:
        print(0)
