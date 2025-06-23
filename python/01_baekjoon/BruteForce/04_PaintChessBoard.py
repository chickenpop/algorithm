# 1018 체스판 다시 칠하기
import sys

n, m = map(int, input().split())
chess_board = [[0 for _ in range(m)]for _ in range(n)]

for i in range(n):  # 체스판을 리스트에 넣는다
    # sys.stdin.readline()으로 입력시 \n도 입력, rstrip 공백 제거
    chess_color = str(sys.stdin.readline().rstrip())
    for j in range(m):
        chess_board[i][j] = chess_color[j]
cnt_list = []  # 칠해야하는 횟수
for i in range(n-7):
    for j in range(m-7):
        cnt_1 = 0  # 칠을 바꿔야하는 횟수, 시작이 'B'또는'W'
        cnt_2 = 0  # cnt_1의 반대 경우
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if chess_board[k][l] != 'B':
                        cnt_1 += 1
                    elif chess_board[k][l] != 'W':
                        cnt_2 += 1
                else:
                    if chess_board[k][l] != 'W':
                        cnt_1 += 1
                    elif chess_board[k][l] != 'B':
                        cnt_2 += 1
        cnt_list.append(min(cnt_1, cnt_2))

print(min(cnt_list))
