# nums = [3,1,3,4,2]
# distinct = set()
# for i in nums:
#     if(i in distinct):
#         print(i)
#         break
#     else:
#         distinct.add(i)

nums = [3,1,3,4,2]

totalSum= 0
sumTillN = 0
for i in nums:
  totalSum +=i
for i in range(len(nums)):
  sumTillN += i
print(totalSum - sumTillN)