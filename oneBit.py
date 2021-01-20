alist = [list of numbers]
adict = []
for i in alist:
    adict.append([i,bin(i).count('1')])
sdict = sorted(adict,reverse = True, key=lambda i: i[1])
ans = []
print(sdict)
for i in sdict:
    ans.append(i[0])
print(*ans)