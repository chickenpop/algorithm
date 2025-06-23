# 4796 캠핑장
import sys
input = sys.stdin.readline
num = 0

while True:
    L, P, V = map(int, input().split()) # 캠핑장 일수 단위, 캠핑장 연속으로 사용가능한 일수, 총 휴가일수

    if (L+P+V) == 0:
        break

    day = (V // P)*L
    if V % P > L:
        day += L
    else:
        day += V % P
    num += 1
    print("Case {}: {}".format(num, day))