# 3052 나머지

lst = []  # 입력된 수의 나머지를 저장할 리스트

for i in range(10):
    num = int(input())
    remainder = num % 42  # 42랑 입력수의 나머지
    lst.append(remainder)

remainder_lst = [0 for _ in range(42)]

for i in lst:
    remainder_lst[i] += 1  # 인덱스랑 같은 나머지값을 만날때마다 +1

cnt = 0
for i in remainder_lst:  # 0~41 사이에 나머지가 1개라도 존재하면 +1
    if i >= 1:
        cnt += 1

print(cnt)
