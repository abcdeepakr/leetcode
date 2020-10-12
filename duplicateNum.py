nums = [3,1,3,4,2]
distinct = set()
for i in nums:
    if(i in distinct):
        print(i)
        break
    else:
        distinct.add(i)