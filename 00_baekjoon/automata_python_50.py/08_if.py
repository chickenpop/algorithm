#9498
score = int(input())

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")

#10817
lst = list(map(int,input().split()))
lst.sort()
print(lst[1])

#11653
n = int(input())
d = 2

while n >= d:
    if n % d == 0:
        print(d)
        n /= d
    else:
        d += 1