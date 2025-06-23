# 2108 통계학
from collections import Counter
import sys

n = int(input())  # 입력되는 수의 갯수
lst = []  # 입력되는 수를 저장할 리스트
for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()

print(round(sum(lst)/n))  # 소수점 이하를 반올림
print(lst[n//2])
mode = Counter(lst).most_common()  # most_common 빈도수 높은 수
if n > 1:  # n이 2개 이상이라면
    if mode[0][1] == mode[1][1]:  # 동일 갯수가 같다면 두번째로 작은수를 출력
        print(mode[1][0])
    else:
        print(mode[0][0])  # 아니라면 첫번째로 많은수를 출력
else:
    print(mode[0][0])
print(max(lst)-min(lst))
