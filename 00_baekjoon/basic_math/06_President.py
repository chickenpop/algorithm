# 2775 부녀회장이 될테야
# 런타임 에러 14층 14호 대한 모든 인원 정보를 채워넣음
import sys
'''
k = int(sys.stdin.readline())        # 아파트 층수
n = int(int(sys.stdin.readline()))
lst = [[0]*15 for i in range(15)] # 리스트 생성

for i in range(15): # k, n의 아파트 인원을 2차원 리스트로 생성
    for j in range(15):
        if i == 0:
            lst[i][j] = j+1
        elif j == 0:
            lst[i][j] = 1
        else:
            lst[i][j] = lst[i][j-1]+lst[i-1][j]
print(lst[k-1][n])
'''
# <성공> 전체가 아닌 k층 n호까지만 리스트를 채워넣어 출력함
TestCase = int(sys.stdin.readline()) # 테스트 케이스 수

for i in range(TestCase):
    k = int(sys.stdin.readline())        # 아파트 층수
    n = int(int(sys.stdin.readline()))   # 아파트 호수

    lst = [[0]*n for i in range(k+1)] # 리스트 생성

    for i in range(k+1): # k, n의 아파트 인원을 2차원 리스트로 생성
        for j in range(n):
            if i == 0:
                lst[i][j] = j+1
            elif j == 0:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i][j-1]+lst[i-1][j]
    print(lst[k][n-1])