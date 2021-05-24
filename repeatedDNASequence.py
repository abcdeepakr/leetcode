class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}
        result = []
        for i in range(len(s)-9):
            if(s[i:i+10] not in hashmap):
                hashmap[s[i:i+10]] = 1
            else:
                hashmap[s[i:i+10]] += 1
        for i in hashmap:
            if hashmap[i] > 1:
                result.append(i)
        return result