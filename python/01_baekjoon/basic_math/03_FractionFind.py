# 1193 분수찾기
line = 0      # 위치하는 라인, 1/1 1부터 시작
max = 0       # 라인에서 가장 큰수

n = int(input())

while n > max :
    line += 1
    max += line

num = max - n
if line % 2 == 0:
    top = line - num    # 분자, top
    under = num + 1     # 분모, under
else :
    top = num + 1
    under = line - num

print("{}/{}".format(top, under))