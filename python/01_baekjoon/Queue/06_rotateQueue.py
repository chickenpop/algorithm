# 1021 회전하는 큐
from collections import deque
import sys

# n = 큐의 크기, m = 뽑아내려는 개수
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))  # 뽑아내려는 큐의 위치


# n 크기의 큐 생성
que = deque()
for i in range(1, n+1):
    que.append(int(i))

cnt = 0  # 2, 3번 수행
for i in lst:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) < len(que)/2:  # 인덱스 위치가 길이의 절반보다 크면 맨뒤에 수를 맨앞으로
                que.rotate(-1)
                print(que)
                cnt += 1
            else:  # 인덱스 위치가 길이의 절반보다 작으면 맨앞의 수를 맨뒤로 이동
                while que[0] != i:  # i이랑 같지 않으면 계속 반복
                    que.rotate(1)
                    cnt += 1

print(cnt)
