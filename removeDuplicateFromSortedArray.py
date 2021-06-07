class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            nums = nums
        if(len(nums) == 0):
            nums = []
        else:
            start = 0
            end = 1
            while(end!=len(nums)):
                if(nums[start]==nums[end]):
                    nums.pop(end)
                else:
                    start = end
                    end = end + 1