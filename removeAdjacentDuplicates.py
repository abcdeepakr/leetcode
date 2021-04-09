string  = "aabbcbdde"
stack = []
for i in string:
  if(stack[len(string)-1] != i):
    stack.append(i)
  else:
    stack.pop()
print("".join(stack))
