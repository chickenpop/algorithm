#8958 OX퀴즈
n = int(input())

for i in range(n):
    lst = str(input())
    cnt = 0
    plus = 1
    for i in range(len(lst)):
        if lst[i] == "O":
            cnt += plus
            plus += 1
        elif lst[i] == "X":
            cnt += 0
            plus = 1
    print(cnt)

#9506 약수들의 합
while True:
    n = int(input())
    d = n-1
    lst = []
    sum = 0

    if n == -1:
        break

    for i in range(n):
        if n % d == 0:
            lst.append(d)
            d -= 1
        else :
            d -= 1
        
        if d == 0:
            break
    
    for i in range(len(lst)):
        sum += lst[i]
    
    if n == sum :
        print(n, "= ", end="")
        lst.reverse()
        for i in range(len(lst)-1):
            print(lst[i], "+ ", end="")
        print(lst[len(lst)-1])
    else :
        print(n,"is NOT perfect.")