nums = [1]
max_ones = 0
if(1 in nums):
    curr_max = 1
else:
    curr_max = 0
for i in range(len(nums)-1):
    if(nums[i]==1 and nums[i+1]==1):
        curr_max +=1
    else:
        max_ones = max(max_ones,curr_max)
print(max_ones)