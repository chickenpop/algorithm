#11047 동전 0
n, k = map(int, input().split())
coin = []

for i in range(n):
    money = int(input())
    coin.append(money)

coin.reverse()
cnt = 0

for i in coin:
    if k // i > 0:
        cnt += k // i
        k = k % i

print(cnt)