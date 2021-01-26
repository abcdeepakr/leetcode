n = int(input())
alist = input().split()
if(type(int(alist[0])%1) == int):
  for i in range(len(alist)):
    alist[i] = int(alist[i])
print(alist)

if(len(alist) == n):
  swaps = {}
  start = 0
  end = n-1
  count = 0
  for i in range(n):
      if(alist[start]<alist[end]):
          start +=1
      else:
          count+=1
          swaps[count] = alist[start]
  if(len(swaps) == 0):
      print(-1)
  elif(len(swaps)>1):
      print(-2)
  else:
      print(swaps[1])
else:
    print(-2)




      