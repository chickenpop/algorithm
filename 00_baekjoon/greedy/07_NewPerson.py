#1946 신입사원
Testcase = int(input())

for i in range(Testcase):
    n = int(input())
    doc_interview = []
    for j in range(n):
        document, interview = list(map(int, input().split()))
        doc_interview.append([document, interview])
        
    doc_interview.sort()
    max = doc_interview[0][1]
    cnt = 0

    for k in range(n):
        if max >= doc_interview[k][1]:
            max = doc_interview[k][1]
            cnt += 1
    print(cnt)
