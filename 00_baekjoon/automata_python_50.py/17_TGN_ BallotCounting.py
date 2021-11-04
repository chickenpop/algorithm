#5063 TGN
n = int(input())
r = [0 for _ in range(n)]
e = [0 for _ in range(n)]
c = [0 for _ in range(n)]

for i in range(n):
    r[i], e[i], c[i] = map(int, input().split())

for i in range(n):
    if r[i] < e[i] - c[i]:
        print("advertise")
    elif r[i] == e[i] - c[i]:
        print("does not matter")
    else:
        print("do not advertise")

#10102 개표
v = int(input())
bal = str(input())
cnt_A = 0
cnt_B = 0

for i in range(len(bal)):
    if bal[i] == "A":
        cnt_A += 1
    else :
        cnt_B += 1

if cnt_A > cnt_B:
    print("A")
elif cnt_A == cnt_B:
    print("Tie")
else:
    print("B")

#10886 0 = not cute / 1 = cute
n = int(input())
lst = []
cnt = 0

for _ in range(n):
    lst.append(int(input()))

for i in range(n):
    if lst[i] == 1:
        cnt += 1

if cnt > (n/2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")