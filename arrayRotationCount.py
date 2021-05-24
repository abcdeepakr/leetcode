'''
Rules

what we get after rotation is a rotated sorted array

position of the minimum element is is the number of times an array has been rotated

if start element is smaller than end element then array is sorted with 0 or multiple of length rotations

if a element in between the array has larger elements on adjacent sides, then it is the smallest element of the list

if mid<= last element then right half is sorted
if mid >= first then everthing on the left till mid is sorted
'''
nums = [4,5,6,7,8,9,10,0,2,3]
#4,5,6,7,8,9,10,0,2,3

low = 0
high = len(nums)-1
smallest = 0
rotationCount = 0
while(1):
  mid = (low+high)//2
  if(nums[low]<nums[high]):
    smallest = nums[low]
    rotationCount = low
    break
  nxt = (mid+1)%len(nums)
  prev = (mid+len(nums)-1)% len(nums)
  if(nums[mid]<nums[prev] and nums[mid]< nums[nxt]):
    smallest = nums[mid]
    rotationCount = mid
    break
  if(nums[mid]<= nums[high]):
    high = mid-1
  if(nums[mid]>=nums[low]):
    low = mid+1
print(smallest,rotationCount)