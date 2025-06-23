# 4344 평균은 넘겠지
# 06은 automata_python_50에서 해결함, 21_OX, 8958번 OX퀴즈 문제다

testcase = int(input())


def s(lst):
    s = 0
    for i in range(1, len(lst)):
        s += lst[i]
    return s


def avg_s(avg, lst):
    s = 0
    for i in range(1, len(lst)):
        if avg < lst[i]:
            s += 1
    result = float(s/lst[0])*100
    return result


for i in range(testcase):
    lst = list(map(int, input().split()))
    avg = s(lst)/lst[0]
    result = avg_s(avg, lst)
    print("%.3f" % result+"%")
