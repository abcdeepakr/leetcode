# class Solution:
    # def bruteForce(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             sums = nums[i] + nums[j]
    #             if(sums==target):
    #                 return [i,j]
  
'''
    def twoSum(self, nums, target):
        alist = []
        for i in nums:
            ans = target - i
            if(ans not in alist):
                alist.append(i)
            else:
                index1 = nums.index(ans)
                index2 = nums.index(i,index1+1)
                return [index1,index2]
    '''
# hashmap Solution
nums = [1,2,3,4,5,6]
target = 9
hashmap = {}
length = len(nums)
for i in range(length):
  resultant = target - nums[i]
  if(resultant in hashmap):
    print([i,resultant])
  else:
    hashmap[nums[i]] = i
