# 15649  N과 M(1)

n, m = map(int, input().split())  # 왜 리스트로 넣지?
s = []


def dfs():
    if len(s) == m:  # 리스트에 길이가 m이랑 같으면 출력
        print(' '.join(map(str, s)))
        return  # 길이가 다르면 함수를 나감

    for i in range(1, n+1):  # 1이상의 자연수부터 n까지
        if i not in s:  # s안에 i가 없으면, 동일 숫자가 없는 경우만 실행
            s.append(i)
            dfs()  # 리스트 내용 출력, 길이가 같다면 if로 넘어감
            s.pop()  # 숫자 하나를 꺼냄


dfs()
