# 2941 크로아티아 알파벳

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]  # 크로아티아 알파벳 변경

word = input()  # 입력 단어

for i in alphabet:
    word = word.replace(i, "A")  # word 안에 i가 있으면 "A"로 바꿔라

print(len(word))
# print(word) replace 결과 확인
