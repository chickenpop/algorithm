# 1181 단어 정렬
import sys

n = int(input())
word = []

for i in range(n):
    word.append(str(sys.stdin.readline().rstrip()))

remove_word = list(set(word))
remove_word.sort()
remove_word.sort(key=len)

for i in remove_word:
    print(i)
