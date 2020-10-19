nums = [1,2,2,2,1,1,1,2,2]
hashmap = {}
for i in nums:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i]+=1
maximum = hashmap[nums[0]]
ans = nums[0]
for j in hashmap:
  if(hashmap[j]>maximum):
    maximum = j
    ans = j
print(ans)