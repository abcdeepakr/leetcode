nums = [0,1,2,3,4,6]
hasharr = [0]*(len(nums)+1)
for i in nums:
    hasharr[i] = 1
for i in range(len(hasharr)):
    if(hasharr[i]==0):
        print(i)