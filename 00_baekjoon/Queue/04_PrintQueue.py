import sys
from collections import deque

TestCase = int(sys.stdin.readline())
for i in range(TestCase):
  n, m = map(int, sys.stdin.readline().split()) #문서갯수, 몇번째로 인쇄되는지 궁금한 문서 
  que = deque(sys.stdin.readline().split()) # 공백문자 남아있음 # 공백제거 큐에 입력  
  m_move = 0
  while que:
    MaxQue = max(que)
    if MaxQue == que[0]:
      m_move += 1
      if len(que) == 1:
        print(m_move)
      que.popleft()
    else:
      data = que.popleft()
      que.append(data)
