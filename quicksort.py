
arr = [80, 60, 30, 90, 40, 50, 70]

pivot = 0
left = 1
right = len(arr)-1

while(1):
  print(arr,left,right)
  if(left == right):
    print (arr)
  else if(arr[left] < arr[pivot]):
    left+=1
  elif(right > left):
    arr[right],arr[left] = arr[left], arr[right]
    
  if(arr[right]>arr[pivot]):
    right+=1
  if(right<left):
    arr[pivot],arr[right] = arr[right],arr[pivot]
