# 18870 좌표압축

n = int(input())  # 좌표 수

x = [int(i) for i in input().rstrip().split()]  # 좌표값 넣기

x_lst = list(set(x))  # 리스트 중복값 제거
x_lst.sort()
x_dict = {}

# 딕셔너리에 좌표값 순서 넣기 ex) [-10, -9, 1, 3] > {-10:0, -9:1 ...}
for i in range(len(x_lst)):
    x_dict[x_lst[i]] = i

for i in x:
    print(x_dict[i], end=" ")  # key값을 넣어 value 출력
