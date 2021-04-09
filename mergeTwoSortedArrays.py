alist = [1,3,4,5,12,18]
blist = [2,6,8,9]
result = []
i = j = 0
length1 = len(alist)
lenght2 = len(blist)

while(i<=len(alist)-1 and j<=len(blist)-1):
  if(alist[i]<blist[j]):
    result.append(alist[i])
    i+=1
  else:
    result.append(blist[j])
    j+=1

if(length1>lenght2):
  for i in range(i,length1):
    result.append(alist[i])
else:
  for i in range(j,lenght2):
    result.append(alist[j])

print(result)