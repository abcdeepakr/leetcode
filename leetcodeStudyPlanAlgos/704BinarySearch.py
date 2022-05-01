class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start+end)//2
        
        if(len(nums) == 1 and nums[0] == target):
            return 0
        
#         while(end-start>1):
#             if(nums[mid] == target):
#                 return mid
#             elif(nums[mid] > target):
#                 end = mid
#                 mid = (start + end)//2
#             elif(nums[mid]<target):
#                 start = mid
#                 mid = (start+end)//2
#         if(nums[start] == target):
#             return start
#         if(nums[end] == target):
#             return end
#         return -1
        while(start<=end):
            if(nums[mid]<target):
                start = mid+1
                mid = (start+end)//2
            elif(nums[mid]>target):
                end = mid-1
                mid = (start+end)//2
            else:
                return mid
        return -1
        
        
            