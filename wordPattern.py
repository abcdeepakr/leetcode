class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashtable = {}
        flag = 0
        words =  s.split()
        set_pattern = len(set(pattern))
        set_words = len(set(words))
        if(len(pattern)!= len(words) or set_pattern!= set_words ):
            return False
        for  i in range(len(pattern)):
          if(pattern[i] not in hashtable):
            hashtable[pattern[i]] = words[i]
          elif(hashtable[pattern[i]] != words[i]):
            flag = 1
            break
        if(flag == 1):
          return False
        else:
          return True