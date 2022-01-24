# 1966 프린터 큐
import sys
from collections import deque

TestCase = int(sys.stdin.readline())
for i in range(TestCase):
  n, m = map(int, sys.stdin.readline().split()) #문서갯수, 몇번째로 인쇄되는지 궁금한 문서 
  que = sys.stdin.readline().strip() # 공백문자 남아있음
  queue = deque(que.replace(" ", "")) # 공백제거 큐에 입력
