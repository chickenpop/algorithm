# 1966 프린터 큐
import sys
from collections import deque

TestCase = int(sys.stdin.readline())
for i in range(TestCase):
  n, m = map(int, sys.stdin.readline().split()) #문서갯수, 몇번째로 인쇄되는지 궁금한 문서 
  que = deque(sys.stdin.readline().split()) # 공백문자 남아있음 # 공백제거 큐에 입력  
  idque = deque(range(0, n))
  m_move = 0
  while que:
    MaxQue = max(que)
    if MaxQue == que[0]:
      m_move += 1
      if idque.popleft() == m:
        print(m_move)
        break
      que.popleft()
    else:
      data = que.popleft()
      que.append(data)
      idque.rotate(-1)
