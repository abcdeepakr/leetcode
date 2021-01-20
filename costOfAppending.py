instructions =[1,2,3,6,5,4]
# nums = []
# nums.append(instructions[0])
# cost = 0
# for i in range(1,len(instructions)):
#   left_nums = 0
#   right_nums = 0
#   for j in range(len(nums)):
#     if(nums[j]<instructions[i]):
#       left_nums+=1
#     elif(nums[j]>instructions[i]):
#       right_nums += 1
#     else:
#       continue
#   cost+=min(left_nums,right_nums)
#   nums.insert(left_nums,instructions[i])
# print(cost)
nums = []
nums.append(instructions[0])
cost = 0
for i in range(1,len(instructions)):
  left_nums = 0
  right_nums = 0
  for j in range(len(nums)):
    if(nums[j]<instructions[i]):
      left_nums+=1
    elif(nums[j]>instructions[i]):
      right_nums += 1
    else:
      continue
  cost+=min(left_nums,right_nums)
  nums.insert(left_nums,instructions[i])
print(cost)