'''
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
      if(len(s)!= len(t)):
          return False
      hashmap = {}
      hashmap2 = {}
      for i in s:
          if(i not in hashmap):
              hashmap[i] = 1
          else:
              hashmap[i]+=1
      for i in t:
          if(i not in hashmap2):
              hashmap2[i] = 1
          else:
              hashmap2[i]+=1
      for i in hashmap:
          if(i in hashmap2):
              if(hashmap[i] == hashmap2[i]):
                  continue
              else:
                  return False
          else:
              return False
      return True
'''
'''
Better solution
'''

def validAnagram(str1, str2):
  if(len(str1) != len(str2)):
    return False
  hashmap = {}

  for i in range(len(str1)):
    print(hashmap)
    if(str1[i] not in hashmap):
      hashmap[str1[i]] = 1
    else:
      hashmap[str1[i]]+=1
    if str2[i] in hashmap:
      hashmap[str2[i]]-=1
    else:
      hashmap[str2[i]] = 1
  for i in hashmap:
    if(hashmap[i] > 0):
      return False
  return True
print(validAnagram("abbc","bcca"))
  