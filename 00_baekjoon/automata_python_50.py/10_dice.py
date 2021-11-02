#2776 주사위 게임
a, b, c = map(int, input().split())

if a == b == c: #눈이 전부 같을때
    print(10000+a*1000)
elif a == b or b == c:
    print(1000+b*100) #눈이 2개 같을때
elif a == c:
    print(1000+a*100)
else: #눈이 전부 다를때
    print(max(a, b, c)*100)
#or 주사위 게임
lst = list(map(int, input().split()))

if lst[0] == lst[1] == lst[2]:
    print(10000+lst[0]*1000)
elif lst[0] == lst[1] or lst[1] == lst[2]:
    print(1000+lst[1]*100)
elif lst[0] == lst[2]:
    print(1000+lst[0]*100)
else:
    print(max(lst)*100)