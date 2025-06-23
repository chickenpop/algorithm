#3009 네 번째 점
x_lst = []
y_lst = []
for i in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)


for i in range(3):
    if x_lst.count(x_lst[i]) == 1:
        x_lst.append(x_lst[i]) 
    if y_lst.count(y_lst[i]) == 1:
        y_lst.append(y_lst[i])

print(x_lst[3], y_lst[3])
# or 직접한거
x = [0 for _ in range(4)]
y = [0 for _ in range(4)]

for i in range(3):
    x[i], y[i] = map(int,input().split())

for i in range(3):
    if x.count(x[i]) == 1:
        x[3] = x[i]
    if y.count(y[i]) == 1:
        y[3] = y[i]

print(x[3], y[3])    