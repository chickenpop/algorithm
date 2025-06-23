#1339 단어 수학
import sys

n = int(sys.stdin.readline())
word = []
dict = {}

for i in range(n): 
    word.append(str(input()))           # n만큼 문자 입력

word.sort(key = len, reverse = True)    # 문자 길이 내림차순 정렬

for i in range(n):
    for j in range(len(word[i])):
        if word[i][j] in dict:
            dict[word[i][j]] += 10**(len(word[i])-j-1)  # 만약 dict에 자릿수만큼 더하기 ex. 'A' = 1000 > 'A' = 1010
        else:
            dict[word[i][j]] = 10**(len(word[i])-j-1)   # dict에 없는 경우 추가하기 ex. 'B' = 100

dic_sort = sorted(dict.items(), key=lambda x:-x[1])     # dict 자릿수가 큰 순서대로 정렬, value기준

num = 9
sum = 0
for i in range(len(dic_sort)): # num = 9~0, dict*num를 더하기
    sum += dic_sort[i][1]*num
    num -=1
print(sum)