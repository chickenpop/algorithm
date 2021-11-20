# 2292

n = int(input())

cnt = 1 # 벌집 수, 본인 포함 ( 1, 7, 19 ) > ( 0, 6, 12 ) 6의 배수씩 벌집이 커진다
count = 1 #이동 칸수

while n > cnt:
  cnt += 6*count
  count += 1

print(count)
