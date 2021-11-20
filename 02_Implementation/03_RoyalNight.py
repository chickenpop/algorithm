# 실전문제 2 왕실의 나이트
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])-ord('a'))+1

right_move = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (1, -2), (-1, -2)]

result = 0
for step in right_move:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)