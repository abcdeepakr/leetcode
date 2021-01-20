s = "0p"
string = ""
for i in s:
    if i.isalnum():
        string += i.lower()
# if(string == string[::-1]):
#   print(1)
# else:
#   print(0)

#two pointer

start = 0
end  = len(string) - 1
flag= 0 
while(start != end):
  if(string[start] == string[end]):
    start +=1
    end -= 1
  else:
    flag = 1
  break
print(True)


