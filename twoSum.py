class Solution:
    # def bruteForce(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             sums = nums[i] + nums[j]
    #             if(sums==target):
    #                 return [i,j]
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