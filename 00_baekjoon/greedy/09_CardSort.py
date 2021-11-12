#1715 카드 정렬하기
n = int(input())
card_lst = []

for i in range(n):
    card_lst.append(int(input()))

card_lst.sort()
num = []
sum = 0
card_sum = card_lst[0] + card_lst[1]
num.append(card_sum)

for i in range(2, n):
    card_sum += card_lst[i]
    num.append(card_sum)

for i in range(len(num)):
    sum += num[i]

print(sum)