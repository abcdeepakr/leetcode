nums = [1,2,3,4,5,6,7]
k = 3
# for i in range(k-1):
#   nums.insert(0,nums[len(nums)-1])
#   nums.pop()
# print(nums)
k%=len(nums)
for i in range(k):
  nums.insert(0,nums[len(nums)-1])
  nums.pop()


  #or
nums = nums[-k:]+ nums[:-k] #is it in O(1) Space