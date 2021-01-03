class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        '''
        using count
        total = 0
        count = 0
        for i in range(1,n+1):
            total +=i
            count +=1
            if(total >=n):
                break
        if(total-n==0):
            return count
        else:
            return count-1
        '''
        
        '''
        using formula
        for i in range(0,n+1):
            equation = (i*(i+1))/2
            if(equation == n):
                return i
                break
            elif(equation>n):
                return i-1
                break
        '''
        #######################
        '''
        using while
        '''
        count = 0
        total = 0
        curr = 1
        while(total<=n):
            total +=curr
            count +=1
            curr +=1
        if(total==n):
            return count
        else:
            return count-1

            
            