n, m = map(int, input().split())

minvalue = 0
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    minvalue = min(data)
    result = max(result, minvalue)

print(result)