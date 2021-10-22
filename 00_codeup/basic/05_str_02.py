# 1408
password = input()
code_1 = ""
code_2 = ""
change = 0

for i in range(len(password)):
    change = ord(password[i])+2
    code_1 += chr(change)
    change = (ord(password[i])*7) % 80 +48
    code_2 += chr(change) 

print(code_1+"\n"+code_2)