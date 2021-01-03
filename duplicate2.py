nums = [1,0,1,1]
k = 1
hashtable = {}
for i in range(len(nums)):
  if nums[i] not in hashtable.values():
    hashtable[i] = nums[i]
  else:
    for key,value in hashtable.items():
      if(nums[i] == value):
        if(abs(i-key)<=k):
          print(True)
        else:
          print(False)
print(hashtable)
for i in hashtable:
  print(i)
for i in range(len(hashtable)):
  print(hashtable[i])

# nums = [1,0,1,1]
# k = 1
# hashtable = {}
# for i in range(len(nums)):
#   if(nums[i] in hashtable and abs(i-hashtable[nums[i]]) <= k):
#     print(True)
#     break
#   else:
#     hashtable[i] = nums[i]
# print(False)

