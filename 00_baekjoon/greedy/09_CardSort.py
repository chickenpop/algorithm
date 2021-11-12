#1715 카드 정렬하기
import heapq

n = int(input())
card_lst = []

for i in range(n):
    heapq.heappush(card_lst, int(input()))

print(card_lst)

sum = 0

while len(card_lst) > 1:
    min1 = heapq.heappop(card_lst)
    min2 = heapq.heappop(card_lst)
    sum += min1 + min2
    heapq.heappush(card_lst, min1+min2)
    print(card_lst)

print(sum)