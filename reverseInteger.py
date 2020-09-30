class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        num = ""
        for i in x:
            if(i.isnumeric()):
                num+=i
        num = int(num[::-1])
        if(num < -2**31 or num>2**31 -1):
            return 0
        else:
            if(int(x)>0):
                return num
            else:
                return -(num)