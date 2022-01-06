# 1157 단어 공부

word = input().lower()
word_list_set = list(set(word))
word_cnt = []

for i in word_list_set:
    cnt = word.count(i)
    word_cnt.append(cnt)

if word_cnt.count(max(word_cnt)) >= 2:
    print("?")
else:
    print(word_list_set[(word_cnt.index(max(word_cnt)))].upper())
