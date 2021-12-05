# 7568 덩치

n = int(input())  # 비교할 인원수
well_built = []

for i in range(n):  # 몸무게와 키를 순서대로 well_built list에 입력
    weight, height = map(int, input().split())
    well_built.append([weight, height])

lst_rank = []
for i in range(n):  # 랭킹 구해주는 반복문, well_built list에 모든 요소를 비교해준다
    rank = 1
    for j in range(n):
        if well_built[i][0] < well_built[j][0] and well_built[i][1] < well_built[j][1]:
            rank += 1
        if j == n-1:
            lst_rank.append(rank)

for i in range(n):
    print(lst_rank[i], end=" ")
