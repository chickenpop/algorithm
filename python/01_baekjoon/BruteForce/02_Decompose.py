# 2231 분해합

n = int(input())  # 어떤 자연수, 1 <= N <= 1,000,000


for i in range(1, n+1):
    s = sum(map(int, str(i)))  # 문자열의 각 자리를 합을 구한다
    s += i                      # sum()+i
    if s == n:                  # 분해합 == n 같으면 출력
        print(i)
        break

    if i == n:                  # i == n, 마지막까지 분해합이 없으므로 0 출력
        print(0)
