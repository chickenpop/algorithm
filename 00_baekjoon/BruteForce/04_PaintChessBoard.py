# 1018 체스판 다시 칠하기
import sys

n, m = map(int, input().split())
chess_board = [[0 for _ in range(m)]for _ in range(n)]

for i in range(n):  # 체스판을 리스트에 넣는다
    # sys.stdin.readline()으로 입력시 \n도 입력, rstrip 공백 제거
    chess_color = str(sys.stdin.readline().rstrip())
    for j in range(m):
        chess_board[i][j] = chess_color[j]
