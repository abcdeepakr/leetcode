'''
n = 5
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5

n = 7
7 7 7 7 7 7 7 7 7 7 7 7 7   
7 6 6 6 6 6 6 6 6 6 6 6 7  n*2 - 2
7 6 5 5 5 5 5 5 5 5 5 6 7  n*2 - 4
7 6 5 4 4 4 4 4 4 4 5 6 7  n*2 - 6
7 6 5 4 3 3 3 3 3 4 5 6 7  n*2 - 8
7 6 5 4 3 2 2 2 3 4 5 6 7  n*2 - 10
7 6 5 4 3 2 1 2 3 4 5 6 7  n*2 - 12
7 6 5 4 3 2 2 2 3 4 5 6 7 
7 6 5 4 3 3 3 3 3 4 5 6 7 
7 6 5 4 4 4 4 4 4 4 5 6 7 
7 6 5 5 5 5 5 5 5 5 5 6 7 
7 6 6 6 6 6 6 6 6 6 6 6 7 
7 7 7 7 7 7 7 7 7 7 7 7 7 
'''
n = 5
op = []
start = str(n)
end = str(n)
curr = n
pre = ""
post = ""
for i in range(2,n*2,2):
  result = start + pre + str(curr-1)*((n*2)-i-1)+post + end
  pre += str(curr-1)
  post = pre[::-1]
  curr -=1
  op.append(result)

print(str(n)*((n*2)-1))
for i in op:
  print(i)
bottomHalf = op[::-1]
for i in range(1,len(bottomHalf)):
  print(bottomHalf[i])
print(str(n)*((n*2)-1))