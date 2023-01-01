class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 700ms solution
        '''
        if(len(nums) == 0):
            first_positive = 0
        else:
            first_positive = int
        flag = False
        
        # find the first positive number
        for i in range(len(nums)):
            if(nums[i]>= 0):
                flag = True
                first_positive = i
                break

        # square the array
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        if(not flag):
            return nums[::-1]
        elif(first_positive == 0):
            return nums
            
        # reverse array upto the first positive number
        nums = nums[:first_positive][::-1] + nums[first_positive:]
        
        # creating two pointers to map over the list and append in new list accordingly
        p,q = 0, first_positive
        sorted_nums = []
        p_len = len(nums[:first_positive])
        q_len = len(nums[first_positive:])
        
        # 2pointer algorithm
        print(nums)
        while(p<p_len and q<len(nums)):
            print("p",p,"q",q)
            print("p",nums[p], "q",nums[q])
            if(nums[p]<=nums[q]):
                print("appending p")
                sorted_nums.append(nums[p])
                p+=1
            else:
                print("appending q")
                sorted_nums.append(nums[q])
                q+=1
        if(p!=p_len):
            for i in range(p,first_positive):
                print("appending p")
                sorted_nums.append(nums[i])
        if(q!=len(nums)):
            print("q",q)
            for i in range(q,len(nums)):
                print("appending q")
                sorted_nums.append(nums[i])
        print("final",sorted_nums)
        return sorted_nums
        
        '''
        # faster solution
        left = 0
        right = len(nums)-1
        sorted_nums = [0] * len(nums)
        index = len(nums)-1
        
        while(left <=right):
            left_sq = nums[left]**2
            right_sq = nums[right]**2
            if(left_sq > right_sq):
                sorted_nums[index] = left_sq
                left+=1
            else:
                sorted_nums[index] = right_sq
                right -=1
            index-=1
        print(sorted_nums)
        return sorted_nums