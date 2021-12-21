# 4673 셀프 넘버

def SelfNumber(num):
    if num > 10000:
        return
    for i in range(1, num+1):
        s = sum(map(int, str(i))) + i
        if s == num:
            break

        if i == num:
            print(num)

    SelfNumber(num+1)


SelfNumber(1)
