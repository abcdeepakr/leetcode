string = "abcd"
output1 = ""
output2 = ""
for i in string:
  output1 += i
  output2 = i + output2
print(output1,output2)