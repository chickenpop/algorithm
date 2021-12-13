# 5-1 stack

from collections import deque

stack = []

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()

stack.append(5)

stack.append(2)

stack.append(3)

stack.append(7)

stack.pop()

stack.append(1)

stack.append(4)

stack.pop()

print('stack 최상단:', stack[::-1])  # 최상단 원소부터 출력

print('stack 최하단:', stack)  # 최하단 원소부터 출력

# 5-2 queue

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삽입()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)  # 먼저 들어온 순
queue.reverse()
print(queue)  # 나중에 들어온 순

# 5-3 recursion


def recursive_function():
    print('재귀 함수를 호출')
    recursive_function()


recursive_function()

# 5-4 recursion 종료 예제


def recursive_function(i):
    # 100번째 호출을 했을 때, 종료되도록 종료 조건 명시
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')


recursive_function(1)
