# 15596 정수 N개의 합
# 기존 for을 활용한 방식                        <런타임 에러>
def IntSum(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

n = int(input())

print(IntSum(n))

# 기본 소스 활용해서 푼 다른 방식 n(n+1) // 2   <런타임 에러>
def solve(a):
    ans = a*(a+1) // 2
    return ans


# 라이브러리에서 sum() 함수를 이용한 방식           <성공>
def solve(a):
    return sum(a)

# range가 아닌 리스트를 활용한 for                 <성공>
def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans
