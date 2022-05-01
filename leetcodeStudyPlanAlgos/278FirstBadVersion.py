# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        '''
        O(n) Linear Search
        for i in range(n):
            if(isBadVersion(i+1)):
                return i+1
        '''

        first = 1
        last = n
        mid = (first + last) // 2

        while (first <= last):

            if (isBadVersion(mid)):

                print(mid, isBadVersion(mid))
                if (isBadVersion(mid - 1) == False):

                    return mid
                last = mid - 1
                mid = (first + last) // 2

            elif (isBadVersion(mid) == False):
                print(mid, isBadVersion(mid))
                first = mid + 1
                mid = (first + last) // 2
            else:
                print(mid, isBadVersion(mid))
                print(first, last)
                return mid
