# 2839 설탕 배달
n = int(input())
cnt = 0   # 배달되는 설탕 봉지 수
error = 0 # 출력 초과를 방지하기 위한 판단 변수

while error < 100:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    elif n < 0:
        print(-1)
        break
    else:
        n -= 3
        cnt += 1
        error += 1