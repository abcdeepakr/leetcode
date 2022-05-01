'''

property of rotated sorted array for searching

after finding mid, any one half will be sorted for sure

set low high and mid

- for right half
if(mid<=high) i.e it is sorted half
  if(target > nums[mid] and target < nums[high])
    then low = mid+1
  else high = mid-1

for left half
if(mid>=low) i.e it is the sorted half
  if(target > nums[low] and target < nums[mid])
    then high = mid-1
  else low = mid+1

'''

nums = [4,5,6,7,8,1,2,3]
target = 8
found = False
low = 0
high = len(nums)-1
while(high - low>=0):
  mid = (low+high)//2
  if(nums[mid] == target):
    found = True
    print(mid)
    break
  if(nums[mid]<= nums[high]):
    if(target<=nums[high] and target>nums[mid]):
      low = mid+1
    else:
      high = mid-1
  if(nums[mid]>=nums[low]):
    if(target>=nums[low] and target < nums[mid]):
      high = mid-1
    else:
      low = mid+1
if(found == False):
  print(-1)
