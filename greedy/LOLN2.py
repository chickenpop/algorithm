n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
frist = array[n-1]
second = array[n-2]

count = 0
result = 0

count += int(m/(k+1))*k
count += m%(k+1)

result += count*frist
result += (m-count)*second

print(result)