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
        cnt = 0  # 칠을 바꿔야하는 횟수
        bw = chess_board[i][j]  # 첫 체스판 색깔
        for k in range(i, i+7):
            for l in range(j, j+7):
                if k % 2 == 0:
                    if l % 2 == 0 and bw != chess_board[k][l]:
                        cnt += 1
                    elif l % 2 == 1 and bw == chess_board[k][l]:
                        cnt += 1
                else:
                    if l % 2 == 0 and bw == chess_board[k][l]:
                        cnt += 1
                    elif l % 2 == 1 and bw != chess_board[k][l]:
                        cnt += 1
            if k == i+6:
                cnt_list.append(cnt)

print(min(cnt_list))
