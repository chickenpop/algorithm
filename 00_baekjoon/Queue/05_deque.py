# 10866 덱
from collections import deque
import sys

n = int(sys.stdin.readline())  # 명령어의 수
queue = deque()

for i in range(n):
    input = list(map(str, sys.stdin.readline().split()))
    if input[0] == 'push_front':
        queue.appendleft(int(input[1]))
    elif input[0] == 'push_back':
        queue.append(int(input[1]))
    elif input[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            queue.popleft()
    elif input[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            queue.pop()
    elif input[0] == 'size':
        print(len(queue))
    elif input[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif input[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
