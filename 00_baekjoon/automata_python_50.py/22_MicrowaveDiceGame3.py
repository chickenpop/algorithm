#10162 전자레인지
abc = []
lst = [300, 60, 10]

cookTime = int(input())

for i in lst:
    d = cookTime // i
    abc.append(d)
    cookTime %= i

if cookTime == 0:
    for i in range(len(lst)):
        print(abc[i], end=" ")
else :
    print(-1)

#10103 주사위 게임
n = int(input())
person1 = 100
person2 = 100

for i in range(n):
    dice1, dice2 = map(int, input().split())

    if dice1 > dice2:
        person2 -= dice1
    elif dice1 < dice2:
        person1 -= dice2

print(person1)
print(person2)

#10214 Baseball
TestCase = int(input())

for i in range(TestCase):
    yonsei = 0
    korea = 0
    for j in range(9):
        y_score, k_score= map(int, input().split())
        yonsei += y_score
        korea += k_score
    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    else :
        print("Draw")