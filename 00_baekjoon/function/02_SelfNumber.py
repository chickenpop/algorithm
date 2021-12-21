# 4673 셀프 넘버

def d(num):
    n = sum(map(int, str(num))) + num
    return n


NoSelfNum = set()

for i in range(1, 10001):
    NoSelfNum.add(d(i))

for i in range(1, 10001):
    if i not in NoSelfNum:
        print(i)
