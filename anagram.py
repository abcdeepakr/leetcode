'''
#My method
string1 = "anagram"
string2 = "nagaram"

hashmap1 = {}
hashmap2 = {}
flag = 0
if(len(string1)!=len(string2)):
  flag  = 1
else:
  for i in range(len(string1)):
    if(string1[i] not in hashmap1):
      hashmap1[string1[i]] = 1
    else:
      hashmap1[string1[i]] += 1
  
  for i in range(len(string2)):
    if(string2[i] not in hashmap2):
      hashmap2[string2[i]] = 1
    else:
      hashmap2[string2[i]] += 1
  for i in range(len(hashmap1)):
    if(string1[i] in hashmap1 and string1[i] in hashmap2):
      if(hashmap1[string1[i]] == hashmap2[string1[i]]):
        flag = 0
    else:
      flag = 1
      break
if(flag == 1):
  print("False")
else:
  print("True")
'''


#one hashmap method

string1 = "anagramm"
string2 = "nagaramn"

hashmap1 = {}
flag = 0
if(len(string1)!=len(string2)):
  flag  = 1
else:
  for i in range(len(string1)):
    if(string1[i] not in hashmap1):
      hashmap1[string1[i]] = 1
    else:
      hashmap1[string1[i]] += 1
  for i in string2:
    if(hashmap1[i] == 0):
      flag = 1
    else:
      hashmap1[i] -=1
if(flag == 1):
  print(False)
else:
  print(True)
