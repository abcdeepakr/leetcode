string = "(()())(())"
result = ""
start_index = 0
left_pt = 0
for index, val in enumerate(string): 
  if(val == "("):
    left_pt += 1
  elif(val == ")"):
    left_pt -= 1
  if(left_pt == 0):
    result += string[start_index+1 : index]
    start_index = index + 1
print(result)
