s = "leetcode"
hashmap = {}
for i in s:
  if(i not in hashmap):
    hashmap[i] = 1
  else:
    hashmap[i]+=1
for i in hashmap:
  if(hashmap[i]==1):
    print(s.index(i))
    break
print(hashmap)
