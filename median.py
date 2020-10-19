# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         arr = nums1+nums2
#         arr.sort()
#         length = len(arr)
#         if(length == 1):
#             return(arr[0])
#         if(length==2):
#             return (arr[0]+arr[1])/2
#         if(length%2!=0):
#             first  = length//2
#             return (arr[first])
#         else:
#             first = length//2
#             second = first - 1
#             return (arr[first]+arr[second])/2
class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    nums = sorted(nums1 + nums2)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    return nums[mid]