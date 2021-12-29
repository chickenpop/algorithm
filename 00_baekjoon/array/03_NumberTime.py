# 2577 숫자의 개수

lst = []  # A, B, C 저장할 리스트

for i in range(3):
    lst.append(int(input()))

num = lst[0]*lst[1]*lst[2]  # A*B*C
number = list(map(int, str(num)))

NumberTime = [0 for _ in range(10)]  # 0~9까지의 개수 저장할 리스트

for i in number:  # 인덱스값과 0~9까지 숫자가 동일하기에 같은 수면 +1
    NumberTime[i] += 1

for i in NumberTime:
    print(i)
