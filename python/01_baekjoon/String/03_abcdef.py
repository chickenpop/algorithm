# 10809 알파벳 찾기

s = str(input())

abc = list(range(97, 123))

for i in abc:
    print(s.find(chr(i)), end=" ")  # find 문자열에서 처음등장한 번호
