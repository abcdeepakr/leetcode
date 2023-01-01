def checkAnagram(word1, word2):
    wordHashmap = {}
    if(len(word1)!=len(word2)):
        return False
    for i in word1:
        if(i not in wordHashmap):
            wordHashmap[i] =1
        else:
            wordHashmap[i]+=1
    for i in word2:
        if(i not in wordHashmap):
            return False
        if(wordHashmap[i] == 0):
            return False
        wordHashmap[i]-=1
    return True


print(checkAnagram("bat","bta"))