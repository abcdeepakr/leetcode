nums =[-1,-2,-9,-6]
maxPositive = nums[0]
maxNegative = nums[0]
maxProduct = nums[0]

for i in range(1,len(nums)):
  choice1 = maxPositive * nums[i] #in kadane we can update in the same line, buthere we have to make sure each iteration same values are passed in the below initializations, hence the value choice1 and choice2
  choice2 = maxNegative * nums[i]
  maxPositive = max(choice1,nums[i],choice2)
  maxNegative = min(choice1,choice2,nums[i])
  maxProduct = max(maxProduct,maxPositive,maxNegative)
print(maxProduct)