money = int(input())

coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
cnt = 0
for i in coin:
    cnt += (money // i)
    money %= i

print(cnt)