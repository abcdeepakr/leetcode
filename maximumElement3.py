import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        length =len(nums)
        for i in nums:
            if(i not in hashmap):
                hashmap[i] = 1
            else:
                hashmap[i]+=1
        for i in hashmap:
            if(hashmap[i]>length/3):
                ans.append(i)
        return ans
#########################################################################################
#moore voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      h = dict()
      majority_ele = []
      n = math.floor(len(nums) / 3)
      for i in nums:
        if i in h:
          h[i] += 1
        else:
          h[i] = 1
      for value, key in h.items():
        if key > n:
          majority_ele.append(value)
      return majority_ele
