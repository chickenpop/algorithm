# 1546 평균

n = int(input())  # 과목의 개수

score = []  # 점수 리스트

score = list(map(int, input().split()))

score_max = max(score)

sum = 0
for i in range(len(score)):
    score[i] = (score[i]/score_max)*100  # 새로운 점수 저장
    sum += score[i]

print(sum/n)  # sum(score)/n 함수를 사용해도 가능, 평균값 바로 출력
