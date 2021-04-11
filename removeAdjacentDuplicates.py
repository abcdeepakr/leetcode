string  = "abbaca"
stack = [string[0]]
entered = 0
for i in range(1,len(string)):
  if(entered == 1):
      entered = 0
      continue
  if(stack[len(stack)-1] == string[i]):
    stack.pop()
    if(stack):
      continue
    elif(i!=len(string)-1):
      stack.append(string[i+1])
      entered = 1
  else:
    stack.append(string[i])
    
print("".join(stack))


#shitcode but works
