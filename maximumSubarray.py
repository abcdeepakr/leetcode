''''
order of n2
a= [-2,1,-3,4,-1,2,1,-5,4]
maximum = 0
for i in range(len(a)):
  current_sum = 0
  for j in range(i,len(a)):
    current_sum +=a[j]
    maximum = max(current_sum,maximum)
print(maximum)

'''
#kadane's algorithm
'''
a= [-2,1,-3,4,-1,2,1,-5,4]
current_sum = a[0]
max_sum = current_sum
for i in range(1,len(a)):
  current_sum = max(current_sum+a[i], a[i])
  max_sum = max(current_sum,max_sum)
print(max_sum)
'''

