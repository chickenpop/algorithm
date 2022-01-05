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

for i in range(1, len(abc)+1):
    if abc[i] > word_max:
        word_max = abc[i]
    elif abc[i] == word_max and word_max > 0:
        print("?")
        break

    if abc[i] == abc[-1]:
        print(chr(abc.index(word_max)+65))
        break
