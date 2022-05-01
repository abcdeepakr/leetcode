class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        
        
        # return
        while(start<=end):
            # check if the target lies in the range
            if(target > nums[end]):
                return end+1
            
            elif(target< nums[start]):
                return start
            # if it does not lie in the above ranges, proceed with binary search
            if(nums[mid]<target):
                start = mid+1
                mid = (start+end)//2
            elif(nums[mid]>target):
                end = mid-1
                mid = (start+end)//2
            else:
                return mid
        