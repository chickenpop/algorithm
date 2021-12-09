# 1181 단어 정렬
import sys


def SameWord(w, lst):
    for i in range(len(lst)):
        if w == lst[i][0]:
            return False
    return True


n = int(sys.stdin.readline())
word = []

for i in range(n):
    wo = str(sys.stdin.readline())
    word_len = len(wo)
    if SameWord(wo, word) == True:
        word.append([wo, word_len])

word_lst = sorted(word, key=lambda x: (x[1], x[0]))

for i in range(len(word_lst)):
    print(word_lst[i][0])
