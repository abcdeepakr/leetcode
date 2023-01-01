# nums =[-1,-2,-9,-6]
# maxPositive = nums[0]
# maxNegative = nums[0]
# maxProduct = nums[0]

# for i in range(1,len(nums)):
#   choice1 = maxPositive * nums[i] #in kadane we can update in the same line, buthere we have to make sure each iteration same values are passed in the below initializations, hence the value choice1 and choice2
#   choice2 = maxNegative * nums[i]
#   maxPositive = max(choice1,nums[i],choice2)
#   maxNegative = min(choice1,choice2,nums[i])
#   maxProduct = max(maxProduct,maxPositive,maxNegative)
# print(maxProduct)

nums = [1, 2]

prefix = []
postfix = [1] * len(nums)
output = []
prefix_product = 1
postfix_product = 1
for i in range(len(nums)):
    prefix_product *= nums[i]
    prefix.append(prefix_product)
for i in range(len(nums) - 1, -1, -1):
    postfix_product *= nums[i]
    postfix[i] = postfix_product

for i in range(len(nums)):
    if (i == 0):
        output.append(postfix[i + 1] * 1)
    elif (i == len(nums) - 1):
        output.append(prefix[i - 1] * 1)
    else:
        output.append(prefix[i - 1] * postfix[i + 1])
print('prefix product', prefix)
print('postfix product', postfix)
print(output)
# [24,12,8,6]
'''
or ones, who did not understand how prefix-postfix works, lets change 1, 2, 3, 4 positions to symbols like a, b, c, d, so multiplying will be:
prefix:
->
|       a       |   a*b   | a*b*c | a*b*c*d |
postfix:
<-
| a*b*c*d | b*c*d |   c*d   |      d        |

the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
|    b*c*d  | a*c*d | a*b*d |   a*b*c   |
'''
