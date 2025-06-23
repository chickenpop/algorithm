#10699 오늘 날짜
import datetime

Now = datetime.datetime.now()  # 갖고 있는 정보 2015-04-19 12:11:32 출력하는 영문자 %Y-%m-%d %H:%M:%S
NowDate =  Now.strftime('%Y-%m-%d')
print(NowDate)

#7287 등록 
# 자신이 백준 온라인 저지에서 맞은 문제의 수와 아이디를 그대로 출력하는 프로그램을 작성하시오
print("46")
print("honeybadger0")

#2525 오븐 시계
hour, min = map(int, input().split())
CookTime = int(input())

hour_Time = (hour*60 + min + CookTime) // 60
min_Time = (hour*60 + min + CookTime) % 60
if hour_Time >= 24:
    hour_Time -= 24 
print(hour_Time, min_Time)

#2530 인공지능 시계
hour, min, sec = map(int, input().split())
CookSec = int(input())

hour += CookSec // 3600
CookSec %= 3600
min += CookSec // 60
CookSec %= 60
sec += CookSec
if sec >= 60:
    min += 1
    sec -= 60
if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour %= 24   

print(hour, min, sec)