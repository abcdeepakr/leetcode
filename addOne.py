class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ""
        output =[]
        for i in digits:
            result += str(i)
        result = str(int(result) + 1)
        for i in result:
            output.append(i)
        return output