alist= [1,2,3,4,3,5,6,1]
adict = set()
for i in alist:
  if(i in adict):
    print(True)
  else:
    adict.add(i)
else:
  print(False)
print(adict)
