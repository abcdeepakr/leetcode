'''
Smallest Positive Integer that can not be represented as Sum 

Input: 
N = 3
array[] = {1, 1, 1}
Output: 
4
Explanation: 
1 is present in the array. 
2 can be created by combining two 1s.
3 can be created by combining three 1s.
4 is the smallest integer value that cannot be 
represented as sum of elements from the array.
 '''
class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here  
        array.sort()
        smallest = 1
        for i in range(n):
            if(array[i]<=smallest):
                smallest += array[i]
        return smallest