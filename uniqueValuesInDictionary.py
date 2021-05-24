arr = [1,1,1,2,3,3]
hashmap = {}
for i in arr:
  if i not in hashmap:
    hashmap[i] = 1
  else:
    hashmap[i] += 1
values = set(hashmap.values())
if(len(values) == len(hashmap)):
  print(True)
else:
  print(False)
