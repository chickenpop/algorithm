# 11729 하노이의 탑 이동 순서

def Hanoi(num, rod1, rod3, rod2):  # 하노이의 탑 알고리즘
    if num == 1:
        print(rod1, rod3)
    else:
        Hanoi(num-1, rod1, rod2, rod3)
        print(rod1, rod3)
        Hanoi(num-1, rod2, rod3, rod1)


n = int(input())  # 원판 갯수

print(2**n-1)  # 총 이동 횟수 2**n-1

Hanoi(n, 1, 3, 2)
