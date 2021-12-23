# 삽입 정렬

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]  # arr = list(map(int, input()))

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:  # 자기보다 작은 데이터를 마주하면 정지
            break

print(arr)
