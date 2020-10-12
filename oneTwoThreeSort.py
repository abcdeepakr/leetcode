nums = [2,0,2,1,1,0]
print(len(nums))
zero = 0
one = 0
two = 0
for i in nums:
    if(i==0):
        zero+=1
    elif(i==1):
        one+=1
    else:
        two+=1
for i in range(zero):
  nums[i] = 0
for j in range(zero,one+zero):
  nums[j] = 1
for k in range(one+zero,len(nums)):
  nums[k] = 2
print(nums)

