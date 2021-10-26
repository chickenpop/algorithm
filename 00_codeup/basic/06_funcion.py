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