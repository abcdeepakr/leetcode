# a = [4,9,5]
# b = [9,4,9,8,4]
# hashmap = {}
# for i in a:
#   if i not in hashmap:
#     hashmap[i] = 1
#   else:
#     hashmap[i]+=1
# print(hashmap)
# for i in b:
#   if i in hashmap:
#     hashmap[i] +=1
# output = []
# for i in hashmap:
#   output.append(str(i) * (hashmap[i]//2))
# output.remove('')
# print(output)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
hashmap = {}
for i in nums1:
  if i not in hashmap:
    hashmap[i] = [1,0]
  else:
    hashmap[i][0]+=1
for i in nums2:
    if i in hashmap:
        hashmap[i][1]+=1
ans = []
for key in hashmap:
    if(hashmap[key][0]> 1 and hashmap[key][1]>1):
        times = min(hashmap[key][0],hashmap[key][1])
        for i in range(times):
            ans.append(key)
print(ans)