class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        flag = 0
        if(target==0 or target<nums[0]):
            return 0
        if(target>nums[len(nums)-1]):
            return len(nums)
        if(nums[mid] == target):
            return mid
        elif(target<nums[mid]):
            for i in range(mid):
                if(nums[i]==target):
                    flag = 1
                    return i
        else:
            for i in range(mid, len(nums)):
                if(nums[i]==target):
                    flag = 1
                    return i
        if(flag == 0 and nums[mid]<target):
            for i in range(mid,len(nums)):
                if(nums[i]<target and nums[i+1]> target):
                    return i+1
        if(flag == 0 and nums[mid]>target):
            for i in range(mid):
                if(nums[i]<target and nums[i+1]> target):
                    return i+1