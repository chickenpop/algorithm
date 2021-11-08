#11557 Yangjojang of The Year
TestCase = int(input())

for i in range(TestCase):
    n = int(input())
    school = []
    alcohol = []
    for j in range(n):
        sch, alco = list(map(str, input().split()))
        school.append(sch)
        alcohol.append(int(alco))
    result = alcohol.index(max(alcohol))
    print(school[result])

#10757
A, B = map(int, input().split())
print(A+B)