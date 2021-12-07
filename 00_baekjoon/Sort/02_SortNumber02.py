# 2751 수 정렬하기 2

# 병합 정렬 Time Out
def mergeSort(x):
    if len(x) > 1:
        mid = len(x)//2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        li, ri, i = 0, 0, 0
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

# 셸 정렬 Time Out


def gapInsertionSort(x, start, gap):
    for target in range(start+gap, len(x), gap):
        val = x[target]
        i = target
        while i > start:
            if x[i-gap] > val:
                x[i] = x[i-gap]
            else:
                break
            i -= gap
        x[i] = val


def shellSort(x):
    gap = len(x) // 2
    while gap > 0:
        for start in range(gap):
            gapInsertionSort(x, start, gap)
        gap = gap // 2


n = int(input())  # n개의 수 입력
lst = []  # n의 수를 저장할 리스트
for i in range(n):
    lst.append(int(input()))

mergeSort(lst)

for i in lst:
    print(i)

shellSort(lst)

for i in lst:
    print(i)
