arr = [1,2,3,4,5]

if(len(arr) <= 1):
  print(arr)
else:
  for i in range((len(arr)//2)):
    print(i)
    arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
  print(arr)