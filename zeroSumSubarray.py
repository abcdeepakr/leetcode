alist = [15,-2,2,-8,1,7,8,10,23] 
alist.sort()
left = 0
right = len(alist)-1

while(left<right):
  sum = alist[left]+alist[right]
  if(sum == 0):
    print([alist[left],alist[right]])
    left +=1
    right -= 1
  elif(sum<0):
    left +=1
  else:
    right -= 1