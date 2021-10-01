n = int(input())
x, y = 1, 1
plan = list(input().split())

#LRUD ¿Ãµø
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for i in plan:
    for move in range(len(move_type)):
        if(i == move_type[move]):
            nx = x + dx[move]
            ny = y + dy[move]
    if(nx < 1 or nx > n or ny < 1 or ny > n):
        continue
    x = nx
    y = ny

print(x, y)