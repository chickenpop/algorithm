# 10809 알파벳 찾기

s = list(map(str, input()))  # 소문자로 이루어진 단어

abc = [-1] * 24  # 알파벳
abc_over = [0] * 24  # 알파벳 중복 여부
cnt = 0

for i in s:
    index = ord(i) - 97
    abc_over[index] += 1
    if abc_over[index] > 1:
        cnt += 1
        continue
    abc[index] = cnt
    cnt += 1

print(abc)
