s = "dvdf"
curr_string = ""
max_len = 0
start = 0
end = 0
while(1):
  if(end == len(s)):
    break
    print(max_len)
  if(s[end] not in curr_string):
    curr_string += s[end]
    end+=1
    max_len = max(max_len, len(curr_string))
  else:
    start+=1
    end = start
    curr_string = ""
print(max_len)