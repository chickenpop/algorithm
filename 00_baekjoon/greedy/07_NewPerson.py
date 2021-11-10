#1946 신입사원
import sys
Testcase = int(input())

for i in range(Testcase):
    n = int(input())
    doc_interview = []
    for j in range(n):
        document, interview = map(int,sys.stdin.readline().split())
        '''
        document, interview = map(int, input().split())
        기존 방식으로 입력을 받으면 시간초과로 인해 실패한다
        '''
        doc_interview.append([document, interview])
        
    doc_interview.sort()
    max = doc_interview[0][1]
    cnt = 0

    for k in range(n):
        if max >= doc_interview[k][1]:
            max = doc_interview[k][1]
            cnt += 1
    print(cnt)