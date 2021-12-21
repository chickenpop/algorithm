# 4673 셀프 넘버

def SelfNumber(num):
    for i in range(1, num+1):
        s = sum(map(int, str(i))) + i
        if s == num:
            break

        if i == num:
            print(num)


for i in range(10001):
    SelfNumber(i)
