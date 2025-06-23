# 10250 ACM 호텔
import sys
TestCase = int(input())

for i in range(TestCase):
    h, w, n = map(int,sys.stdin.readline().split()) # 층수, 호수, 손님 입장 번호
    cnt = 0
    high = 1                    # 손님의 호텔 층수
    room = 1                    # 손님의 호텔 방번호(호수)
    for j in range(1, w+1):
        for k in range(1, h+1):
            cnt += 1
            high = k
            room = j
            if cnt == n:
                break
        if cnt == n:
                break
    print("{}{:02d}".format(high, room))