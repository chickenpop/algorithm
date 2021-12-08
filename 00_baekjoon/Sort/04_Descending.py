# 1427 소트인사이드 (내림차순)

number = str(input())

number_lst = map(int, number)

number_sort = sorted(number_lst, reverse=True)

for i in number_sort:
    print(i, end="")
