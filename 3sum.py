nums = [-1,0,1,2,-1,-4]
ans = []
for i in range(len(nums)):
  target = nums[i]
  read = []
  for j in range(i+1,len(nums)):
    twosum = target + nums[j]
    if(twosum not in read):
      read.append(nums[j])
    else:
      ans.append([target,twosum,nums[j]])
print(ans)

