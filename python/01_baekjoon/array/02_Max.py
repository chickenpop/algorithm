# 2562 최댓값

lst = []

for i in range(9):
    lst.append(int(input()))
lst_max = max(lst)  # 최댓값

for i in range(len(lst)):
    if lst_max == lst[i]:
        index = i  # 최댓값 인덱스 저장

print(max(lst))
print(index+1)
