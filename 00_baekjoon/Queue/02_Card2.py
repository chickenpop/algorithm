# 2164 카드 2
from collections import deque
import sys

n = int(sys.stdin.readline())
que = deque([i for i in range(1, n+1)])  # queue 사용하면 import queue 자동으로 입력됨

while que:
    if len(que) == 1:
        print(que[0])
        break
    else:
        que.popleft()
        MoveRightCard = que.popleft()
        que.append(MoveRightCard)
