# 1526 함수로 hello 문자열 출력하기
def hello():
    print("hello")
    
hello()

#1527 함수로 123 값 출력하기
def IntPrint():
    print("123")
    
IntPrint()

#1528 함수로 *문자 출력하기 
def star():
    print("*")
    
star()

#1529 함수로 **문자 출력하기
def doublestar():
    print("**")
    
doublestar()

#1530 함수로 문자 A 리턴하기
def A():
    return "A"

result = A()
print(result)


#1531 함수로 정수(int) 1 리턴하기
def one():
    return 1 

result = one()
print(result)

#1532 함수로 정수(long long int) 리턴하기
def longlongint():
    return -2147483649
    
result = longlongint()
print(result)

#1533 함수로 실수(float) 3.14 리턴하기
def pie():
    return 3.14
    
result = pie()    
print("%f"%result)

#1534
def f():
    return 3.1415926535897
    
print(f())

#1535 함수로 가장 큰 값 위치 리턴하기
def max_pos():
    max_p = d[0]
    cnt = 0
    for i in range(n):
        if max_p < d[i]:
            max_p = d[i]
            cnt = i
    return cnt+1

n = int(input())
d = list(map(int, input().split()))

print(max_pos())

#1536 함수로 가장 작은 값 리턴하기
def min_pos():
    min_p = d[0]
    for i in range(len(d)):
        if min_p > d[i]:
            min_p = d[i]
    return min_p

n = int(input())
d = list(map(int, input().split()))

print(min_pos())