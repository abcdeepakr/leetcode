nums = [12,4,324,23,53,45,3,234,54,4,4,4,3,3,3,4,45,5,6,6,7,5,34,23,4,6,7,4,3,2,5,7,7,3,2,1] 
if(len(nums) == 0):
    print(0) 
if(len(nums) == 1):
    print(1) 
longestStreak = 1
hashmap = {}
for i in nums:
    if(i not in hashmap):
        hashmap[i] = 1
    else:
        hashmap[i] +=1
for i in nums:
    if(i-1 not in hashmap):
        currVal = i
        currStreak = 1
        
        while(currVal+1 in hashmap):
            currVal +=1
            currStreak +=1
        longestStreak = max(longestStreak,currStreak)
print(longestStreak) 
        