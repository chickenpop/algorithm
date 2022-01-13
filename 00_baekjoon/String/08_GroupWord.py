# 1316 그룹 단어 체커

n = int(input())  # 단어 갯수
word = [0 for i in range(n)]

for i in range(n):
    word[i] = input()

cnt = 0
for i in word:
    NoStack = 0
    lst = list(map(str, i))
    for j in lst:
        NewWord = lst.count(j)
        if NewWord >= 2:
            FirstIndex = i.find(j)
            LastIndex = i.rfind(j)
            if NewWord != (LastIndex-FirstIndex+1):
                NoStack += 1
    if NoStack == 0:
        cnt += 1


print(cnt)
