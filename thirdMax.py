#2ND MAX ALG0


def secondMax(alist):
  biggest = max(alist[0],alist[1])
  secondBiggest = min(alist[0],alist[1])
  for i in range(2,len(alist)):
    if(alist[i]> biggest):
      secondBiggest = biggest
      biggest = alist[i]
    elif(alist[i]>secondBiggest and alist[i]!=biggest):
      secondBiggest = alist[i]
  print(secondBiggest)

# alist = [1,2,3,4,3,4,5,6,5,6,12,7,15,67,78,76] 
list1 = [2, 2, 3, 1]

# mx=max(list1[0],list1[1]) 
# secondmax=min(list1[0],list1[1]) 
# n =len(list1) 
# for i in range(2,n): 
# 	if list1[i]>mx: 
# 		secondmax=mx 
# 		mx=list1[i] 
# 	elif list1[i]>secondmax and mx != list1[i]: 
# 		secondmax=list1[i] 
# 	else: 
# 		if secondmax == mx: 
# 			secondmax = list1[i] 

print("Second highest number is : ",str(secondMax))