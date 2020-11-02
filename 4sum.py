nums =[-3,-2,-1,0,0,1,2,3]
target = 0
ans = []
nums.sort()
for i in range(len(nums)):
  for j in range(i+1,len(nums)):
    front = j+1
    back = len(nums)-1
    remaining = target - (nums[i]+nums[j])
    while(front<back):
      two_sum = nums[front]+nums[back]
      if(two_sum<remaining):
        front +=1
      elif(two_sum>remaining):
        back-=1
      else:
        ans.append([nums[i],nums[j],nums[front],nums[back]])
        back-=1
final = []
for i in ans:
    if(i not in final):
        final.append(i)
print(final)
        