'''
Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9 .

Input:
N = 9
Output:
10
Explanation:
After removing natural numbers which contains
digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10
and 9th number is 10.
'''

n = 8
i = 1
count = 0
ans = 0
nine_count = 0
while(1):
  if(count==n):
    print(ans+nine_count)
    break
  else:
    if("9" not in str(i)):
      count+=1
      i+=1
      ans = count
    else:
      i+=1
      nine_count+=1