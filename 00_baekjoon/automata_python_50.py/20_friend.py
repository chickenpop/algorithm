#5717 상근이의 친구들
while True:
    male, female = map(int,input().split())

    if male == 0 and female == 0:
        break

    print(male+female)

#9610 사분면
n = int(input())
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0
for i in range(n):
    x, y = map(int, input().split())

    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1
    else:
        axis += 1

print("Q1:", q1)
print("Q2:", q2)
print("Q3:", q3)
print("Q4:", q4)
print("AXIS:", axis)