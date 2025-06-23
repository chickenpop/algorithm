#13305 주유소
city = int(input())
km = list(map(int, input().split()))
gas = list(map(int, input().split()))

min_cost = 0
min_gas = gas[0]
for i in range(city-1):
    if min_gas > gas[i]:
        min_gas = gas[i]
    min_cost += min_gas * km[i]

print(min_cost)