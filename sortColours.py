class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sore()
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
        # nums = [0]*zero + [1]*one+[2]*two\
        for i in range(zero):
          nums[i] = 0
        for j in range(zero,one+zero):
          nums[j] = 1
        for k in range(one+zero,len(nums)):
          nums[k] = 2