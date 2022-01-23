# 11866 요세푸스 문제 0
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queInput = deque([i for i in range(1, n+1)])
que_lst = []

while queInput:
    queInput.rotate(-k)  # 큐를 k만큼 회전시킴
    que_lst.append(str(queInput.pop()))  # .join 사용을 위해 string으로 삽입

print("<", ", ".join(que_lst), ">", sep="")  # 구분기호 사용 .join, sep 공백제거
