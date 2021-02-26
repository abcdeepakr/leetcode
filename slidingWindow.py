#n squared
'''
import time
begin   = time.time()
alist = [1,2,3,4,2,3,4,2,4,6,8,56,3,5,7,4]
num = 3
max_sum = 0
for i in range(len(alist)-num):
  temp = 0
  for j in range(i,i+num):
    temp+=alist[j]
  max_sum = max(temp,max_sum)
print(max_sum)
end = time.time()
print(end-begin)
'''

# linear time using sliding window
import time
begin   = time.time()
alist = [1,2,3,4,2,3,4,2,4,6,8,56,3,5,7,4]
num = 3
max_sum = 0
temp = max_sum
for i in range(num):
  temp+=alist[i]
for i in range(len(alist)-num):
  temp = temp - alist[i] + alist[i+num]
  max_sum = max(temp,max_sum)
print(max_sum)
end = time.time()
print(end-begin)