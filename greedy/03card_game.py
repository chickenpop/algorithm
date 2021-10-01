n, m = map(int, input().split())

minvalue = 10001

for i in range(n):
    data = list(map(int, input().split()))
    for a in data:
        minvalue = min(data)

print(minvalue)