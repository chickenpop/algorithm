# 1157 단어 공부

word = list(str(input()))
word_upper = []
abc = [0] * 27
abc[26] = -1
for i in word:
    word_upper.append(i.upper())

for i in word_upper:
    index = ord(i) - 65
    abc[index] += 1

word_max = abc[0]
for i in abc:
    if i != abc[0] and i > word_max:
        word_max = i
    elif i != abc[0] and i == word_max:
        print("?")
        break
    if i == abc[-1]:
        print(chr(abc.index(word_max)+65))
        break
