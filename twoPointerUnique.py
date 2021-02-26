alist = [1,2,3,4,5,1,2,3,7,8,4,5]
alist.sort()
i = 0
j = 1

for j in range(len(alist)):
  if(alist[i] == alist[j]):
    j+=1
  else:
    i +=1
    alist[i] = alist[j]
print("total unique elements are" ,i+1)