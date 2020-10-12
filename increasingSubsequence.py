nums = [s]
longest = 0
curr_max = 1
if(len(nums)<1):
    print(0)
else:
    last = nums[0]
    for i in range(len(nums)-1):
        if(nums[i+1]>nums[i]):
            curr_max +=1
        else:
            if(curr_max>longest):
                longest = curr_max
                last = nums[i]
                curr_max = 1
print(max(longest,curr_max))