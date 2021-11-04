#7567 그릇
bowl = str(input())
cnt  = 10

for i in range(1, len(bowl)):
    if bowl[i] != bowl[i-1]:
        cnt += 10
    else:
        cnt += 5
    
print(cnt)