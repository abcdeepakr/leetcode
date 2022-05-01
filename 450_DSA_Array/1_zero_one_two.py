
def sort012(arr,n):
  zero = arr.count(0)
  one = arr.count(1)
  
  for i in range(n):
      if(i<zero):
          arr[i] = 0
      elif(i<zero + one):
          arr[i] = 1
      else:
          arr[i] = 2
  print(arr)
sort012([1,0,0,2,2,1,0,1,1,1,1], 11 )