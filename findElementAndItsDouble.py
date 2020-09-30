class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    if(arr.count(0)==2):
        return True
    else:
        for i in arr:
            if(i==0):
                continue
            elif(i*2 in arr):
                return True
        else:
            return False

          