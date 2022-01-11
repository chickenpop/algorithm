# 5622 다이얼

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQS', 'TUV', 'WXZ']

word = list(input())
time = 0

for i in word:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3

print(time)
