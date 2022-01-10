# 2908 상수

word_a, word_b = map(list, input().split())  # 상수를 리스트로 입력

# 상수 뒤집기
word_a.reverse()
word_b.reverse()

# 출력
if word_a > word_b:
    for i in word_a:
        print(i, end="")
else:
    for i in word_b:
        print(i, end="")
