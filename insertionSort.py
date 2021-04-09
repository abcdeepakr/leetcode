alist = [11,3,4,5,6,3,2,4,5,7,7,54,3,2,45,6,67]

for i in range(1,len(alist)):
  current_index = i
  current_element = alist[i]
  while(1):
    if(alist[i-1]>alist[current_index] and i>=0):
      i-=1
    else:
        break
    if(i==0):
        break
  alist.pop(current_index)
  alist.insert(i,current_element)
    
print(alist)
