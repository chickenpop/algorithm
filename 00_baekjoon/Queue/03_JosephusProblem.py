# 11866 요세푸스 문제 0
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queInput = deque([i for i in range(1, n+1)])
queOutput = deque()
index = n - k

while queInput:
    if len(queInput) == n:
        queInput.rotate(index)
    else:
        queInput.rotate(k)  # 큐를 k만큼 회전시킴
    print(queInput)
    queOutput.append(queInput.pop())

print(queOutput)
