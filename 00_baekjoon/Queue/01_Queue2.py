# 18258 큐 2

from collections import deque  # 데이터를 양방향에서 추가하거나 제거가능한 자료구조
import sys
# queue = deque([1, 2, 3])  # 생성
# print("생성{}".format(queue))
# queue.append(4)  # 삽입
# print("삽입 뒤{}".format(queue))
# queue.appendleft(0)
# print("삽입 잎{}".format(queue))
# queue.popleft()  # 제거
# print("제거{}".format(queue))

n = int(sys.stdin.readline())  # 명령 총 횟수
queue = deque()  # 빈 큐 생성
list = []  # 결과 출력 리스트
for i in range(n):
    Input = list(map(str, sys.stdin.readline().split()))
    if Input[0] == "push":
        queue.append(Input[1])
    elif Input[0] == "pop":
        if len(queue) == 0:
            list.append(-1)
        else:
            queue.popleft()
    elif Input[0] == "size":
        list.append(len(queue))
    elif Input[0] == "empty":
        if len(queue) == 0:
            list.append(1)
        else:
            list.append(0)
    elif Input[0] == "front":
        if len(queue) == 0:
            list.append(-1)
        else:
            list.append(queue[0])
    elif Input[0] == "back":
        if len(queue) == 0:
            list.append(-1)
        else:
            list.append(queue[-1])

for i in list:
    print(i)
