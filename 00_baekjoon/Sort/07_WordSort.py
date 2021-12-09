# 1181 단어 정렬
# import sys

# n = int(input())
# word = []

# for i in range(n):
#     word.append(str(sys.stdin.readline().rstrip()))

# remove_word = list(set(word))
# remove_word.sort()
# remove_word.sort(key=len)

# for i in remove_word:
#     print(i)

# short code

n = int(input())
word = set()

for i in range(n):
    wo = str(input())
    word.add((wo, len(wo)))  # set에 값 추가 add 2차원 넣기 ()

word_lst = list(word)
word_lst.sort(key=lambda x: (x[1], x[0]))

for i in word_lst:
    print(i[0])
