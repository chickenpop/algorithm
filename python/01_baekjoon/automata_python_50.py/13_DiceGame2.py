#2476 주사위 게임
n = int(input())
winner = 0
result = 0

for i in range(n):
    lst = list(map(int, input().split()))
    if lst[0] == lst[1] == lst[2]:
        result = 10000+lst[0]*1000
    elif lst[0] == lst[1] or lst[1] == lst[2]:
        result = 1000+lst[1]*100
    elif lst[0] == lst[2]:
        result = 1000+lst[0]*100
    else:
        result = max(lst)*100
    if winner < result:
        winner = result

print(winner)