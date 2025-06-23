# 10814  나이순 정렬
import sys

n = int(input())  # 회원가입자 수
member = []  # 가입자 정보
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    member.append([int(age), name])  # 나이, 이름으로 리스트 넣기

member.sort(key=lambda x: x[0])  # 나이순으로만 정렬

for i in member:
    print(i[0], i[1])
