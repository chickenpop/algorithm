# 10989 수 정렬하기 3
import sys

n = int(sys.stdin.readline())
number = [0] * 10001  # 조건은 10000이하의 수라서 +1

for i in range(n):
    num = int(sys.stdin.readline())
    number[num] += 1  # 입력된 수와 같은 리스트에 +1

for i in range(10001):
    if number[i] != 0:
        for _ in range(number[i]):  # 리스트 크기만큼 출력
            print(i)
