words = ["i", "love", "leetcode", "i", "love", "coding"]
key = 2
hashtable = {}
for i in words:
  if(i not in hashtable):
    hashtable[i] = 1
  else:
    hashtable[i] +=1
# ans = sorted(hashtable.items(),key = lambda kv:(kv[1], kv[0]), reverse = True)
# final  = []
# for i in range(key):
#   final.append(ans[i][0])
# print(sorted(final))