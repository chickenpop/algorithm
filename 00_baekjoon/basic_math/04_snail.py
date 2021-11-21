# 2869 달팽이는 올라가고 싶다
import sys
a, b, v = map(int,sys.stdin.readline().split())
v_sum = 0 # 달팽이 위치
cnt = 0   # 걸리는 일수

while v_sum <= v:
    cnt += 1
    v_sum += a
    if v_sum >= v:
        break
    else:
        v_sum -= b

print(cnt)