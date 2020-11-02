arr = [2,2,2,3,3,3]
ans = 0
for i in arr:
    if(arr.count(i)==i and i > ans):
        ans = i
print(ans)