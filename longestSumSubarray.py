#finding the maximum subarray sum 
'''
nums =  [-2,1,-3,4,-1,2,1,-5,4]
curr_sum = nums[0]
max_sum = curr_sum
prev_index = curr_index = 0
for i in range(1, len(nums)):
  curr_sum = max(curr_sum + nums[i] , nums[i])
  max_sum = max(curr_sum, max_sum)
# print(max_sum)
'''
#finding the subarray with max sum
#same input

nums =  [-2,1,-3,4,-1,2,1,-5,4,18]
maximum_element = max(nums)
if(maximum_element<0):
  print(maximum_element)
curr_sum = max_sum = 0
start = end = 0
beginning = 0 #will reset everytime we move to a new subarray

for i in range(len(nums)):
  curr_sum += nums[i]
  if(curr_sum < 0):
    curr_sum = 0
    beginning = i + 1
  if(curr_sum> max_sum):
    max_sum = curr_sum
    start = beginning
    end = i
print(nums[start : end+1])