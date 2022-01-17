# 4949 균형잡힌 세상

stack = [1]

while stack[0] != 0:
  stack = []
  Input = list(map(str, input()))
  for i in Input:
    if i == "(":
      stack.append(1)
    elif i == ")":
      stack.append(-1)
    elif i == "[":
      stack.append(1.3)
    elif i == "]":
      stack.append(-1.3)
    elif i == ".":
      stack.append(0)
    else:
      continue
    if sum(stack) < 0:
      print("NO")
      break
  if sum(stack) == 0 and stack[0] != 0:
    print("YES")
  elif stack[0] != 0 and sum(stack) > 0:
    print("NO")
    
